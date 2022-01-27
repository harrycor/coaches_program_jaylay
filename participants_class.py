import json
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# PARTICIPANTS DATA **** this will not be the final list - this will only ret info needed to complete JSON
# ***SPECIFIED EVENT PAGE must work for ALL event urls***
# TODO get- paring pool que. weight range. for each event
# TODO go to total participants url > 'get id num' then go to participants page > get age, team, weight, WAR
# TODO wrestlers: name; id (get from full list of participants), age, team, weight, war
# TODO to create json for each team

# Constants
# "event num/demo even" will be diff
"https://test.wrestlingrating.com/event/174/participants/"
MAIN_SITE_ADDY = "https://test.wrestlingrating.com"
# EVENT_URL = "/174/demonstration-event/"
# PARTICIPANTS_LIST_URL = "/event/174/participants/"
INNER_LOOP_REFERENCE_URL = "/event/"
# EVENT = MAIN_SITE_ADDY + INNER_LOOP_REFERENCE_URL + EVENT_URL

ISO_EVENT_NAME = "event name pending"

ID = "id"
NAME = "name"
WEIGHT = "weight"
AGE = "age"
WAR = "WAR"
PLAYER_PAGE = "url"

# final JSON for participants list not by teams


class ParticipantsInfoForSend:

    def __init__(self, eu):
        self.participants_list_event = self.gather(eu)

    def gather(self, event_url):
        # Pulls HTML data (event page) for scraping
        response_event = requests.get(MAIN_SITE_ADDY + event_url, verify=False)
        response_event.raise_for_status()
        event_html = response_event.text  # HTML text
        # print(events_html)
        soup_event = BeautifulSoup(event_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping

        # event HTML url
        participants_href_html = soup_event.find_all(name="div", class_="col s12 m4")[1]("a")
        # print(participants_href_html)

        #  getting participants URL href no html - list
        participants_url_list = []  # list of URL's
        for body_loop in participants_href_html:
            limbo = []  # placeholder for participants page url, empties once put in event_hrefs
            route_num = 0  # used to direct if statements
            # print(body_loop)
            if INNER_LOOP_REFERENCE_URL in str(body_loop):  # if "/event" is in body_loop, inner loop executes
                for anchor_loop in str(body_loop):
                    # print(h)
                    if anchor_loop == "\"":
                        route_num += 1
                    if route_num == 1:
                        if anchor_loop == "\"":
                            pass
                        else:
                            limbo.append(anchor_loop)  # adds character to limbo list eg: 'e', 'v', 'e', 'n', 't'
                    if route_num == 2:
                        combined = "".join(limbo)  # joins characters in limbo to make single str
                        # print(combined)
                        participants_url_list.append(combined)  # adds string to events_hrefs then breaks out of loop
                        break  # and resets limbo for next item
        participants_url_to_str = ""
        for url_to_str in participants_url_list:
            participants_url_to_str = url_to_str
        participants_final_url = MAIN_SITE_ADDY + participants_url_to_str
        # print(participants_final_url)
        # probably would return this url to def

        # go to participants list
        # Pulls HTML data (participant page) for scraping
        response_participants = requests.get(participants_final_url, verify=False)
        response_participants.raise_for_status()
        participants_html = response_participants.text  # HTML text
        soup_participants = BeautifulSoup(participants_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping

        # iso list data
        iso_participant_data_html = soup_participants.select(selector="tbody tr td")
        # print(iso_participant_data_html)

        # creates list of player data from html iso list
        participants_list = {

        }
        participant_data_placeholder = []

        for p_list_grabber in iso_participant_data_html:
            participant_data_placeholder.append(p_list_grabber.text)

        ret_this_dict = {}

        # print(participant_data_placeholder)
        # for x in participant_data_placeholder:
        #     print(x)

        part_num = 1
        route_num = 0
        player_placeholder = []
        for x in participant_data_placeholder:
            if route_num <= 4:
                player_placeholder.append(x)
                route_num += 1
                if route_num == 5:
                    # create dict_obj
                    player_id = player_placeholder[0]
                    name_before = player_placeholder[1]
                    name = name_before.replace(" ", "-")
                    weight = player_placeholder[2]
                    age = player_placeholder[3]
                    war = player_placeholder[4]
                    name_1 = name.replace("\"", "")
                    name_2 = name_1.replace("\'", "")
                    name_for_url = name_2.replace("/", "")
                    url = f"/{player_id}/{name_for_url}"
                    ret_this_dict[part_num] = {ID: player_id, NAME: name_before, WEIGHT: weight, AGE: age, WAR: war,
                                               PLAYER_PAGE: url}
                    part_num += 1
                    route_num = 0
                    player_placeholder = []

        return ret_this_dict
