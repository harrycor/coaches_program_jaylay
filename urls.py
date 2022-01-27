import json
from bs4 import BeautifulSoup
import requests
#
# # ****TODO ABSOLUTE MUST - ":" isnt being read by python correctly. can fix this easy if I remember correctly.
# # TODO maybe reorder the event title, date, location list before creating it for easier iteration during JSON creation
#
# # Constants
# EVENTS_URL = "https://test.wrestlingrating.com/events/"
#
# DATE = "date"
# LOCATION = "location"
# URL = "url"
#
# INNER_LOOP_REFERENCE_URL = "/event/"
#
# # Data to create JSON
# data_dict_for_json = {
#     "events": {
#
#     }
# }
#
#
# # Pulls HTML data for scraping
# response = requests.get(EVENTS_URL, verify=False)
# response.raise_for_status()
# events_html = response.text  # HTML text
# # print(events_html)
# soup_events = BeautifulSoup(events_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping
# tbody_data = soup_events.select(selector="p tbody tr td")    # table data from tbody (events info) (list)
# # print(tbody_data)
#
#
# # URL's list
# event_hrefs = []    # list of URL's
# for body_loop in tbody_data:
#     limbo = []      # placeholder for event url, empties once put in event_hrefs
#     route_num = 0         # used to direct if statements
#     # print(body_loop)
#     if INNER_LOOP_REFERENCE_URL in str(body_loop):     # if "/event" is in body_loop, inner loop executes
#         for anchor_loop in str(body_loop):
#             # print(h)
#             if anchor_loop == "\"":
#                 route_num += 1
#             if route_num == 1:
#                 if anchor_loop == "\"":
#                     pass
#                 else:
#                     limbo.append(anchor_loop)   # adds character to limbo list eg: 'e', 'v', 'e', 'n', 't'
#             if route_num == 2:
#                 combined = "".join(limbo)       # joins characters in limbo to make single str
#                 # print(combined)
#                 event_hrefs.append(combined)    # adds string to events_hrefs then breaks out of loop
#                 break                               # and resets limbo for next item
# # print(event_hrefs)
#
#
# # DATE, EVENT NAME, LOCATION list, there is a REASON it was made separate this way
# event_date_name_local = []  # list of event-title, date, location, in that order
# # this loop strips HTML
# for stripper_loop in tbody_data:
#     stripper_loop = stripper_loop.text.strip("\n")  # REASON - no href when 'stripped' - **must strip to isolate event
#     try:
#         int(stripper_loop)
#     except ValueError:
#         event_date_name_local.append(stripper_loop)
#         # print(y)
#     else:
#         pass
#     # print(stripper_loop)
# # print(event_date_name_local)
#
#
# # dictionary data for JSON. uses event-title, date, name, location list, PLUS URL list to compile data
# event_placeholder = []    # used as placeholder to load each events info before adding to dict. emptied each loop around
# marker_event = 0        # acts as if router
# marker_url = 0
# for create in event_date_name_local:
#     if marker_event <= 2:
#         # print(create)
#         # print("*************")
#         event_placeholder.append(create)    # adds event-title, date, location to placeholder
#         if marker_event == 2:
#             try:
#                 event_placeholder.append(event_hrefs[marker_url])   # adds event URL to placeholder
#                 marker_event = 0    # resets routing
#                 marker_url += 1     # ensure correct URL is added to event
#                 # print(event_maker)
#
#                 # sets variables  for dict placement
#                 date_event_maker = event_placeholder[0]
#                 event_event_maker = event_placeholder[1]
#                 location_event_maker = event_placeholder[2]
#                 url_event_maker = event_placeholder[3]
#
#                         # Dictionary for JSON
#                 data_dict_for_json["events"][event_event_maker] = {DATE: date_event_maker,
#                                                                    LOCATION: location_event_maker,
#                                                                    URL: url_event_maker}
#
#                 event_placeholder = []      # resets placeholder for next event
#             except:     # for when event_hrefs index is out of range * change?
#                 pass
#         else:
#             marker_event += 1   # increases for routing (2 re-routes it)
#
# # JSON used from dictionary data
# json_event = json.dumps(data_dict_for_json, indent=4)
# print(json_event)
# # print("all good")


# with open(file="docs/references/events_data_inactive.json", mode="w") as file:
#     json.dump(data_dict_for_json, file, indent=4)

# event page for a specific event (the demonstration event)
#   pool weight range (at the top), the pairing pool, the link to the participant's list,
#   and the on deck matches for each mat = https://test.wrestlingrating.com/event/174/demonstration-event/      (this is just a sample)

# participants page for (the demonstration event),
#   wrestlers weights, ages, and WAR (weight adjusted ratings). = https://test.wrestlingrating.com/event/174/participants/

# rankings page, lists every wrestler in our database along with their team names = https://test.wrestlingrating.com/rankings/









#  *************************************************************************************************************

# # PARTICIPANTS DATA **** this will not be the final list - this will only ret info needed to complete JSON
# # ***SPECIFIED EVENT PAGE must work for ALL event urls***
# # TODO get- paring pool que. weight range. for each event
# # TODO go to total participants url > 'get id num' then go to participants page > get age, team, weight, WAR
# # TODO wrestlers: name; id (get from full list of participants), age, team, weight, war
# # TODO to create json for each team
#
# # Constants
# # "event num/demo even" will be diff
# "https://test.wrestlingrating.com/event/174/participants/"
# MAIN_SITE_ADDY = "https://test.wrestlingrating.com"
# EVENT_URL = "/174/demonstration-event/"
# # PARTICIPANTS_LIST_URL = "/event/174/participants/"
# INNER_LOOP_REFERENCE_URL = "/event/"
# EVENT = MAIN_SITE_ADDY + INNER_LOOP_REFERENCE_URL + EVENT_URL
#
# ISO_EVENT_NAME = "event name pending"
#
# ID = "id"
# NAME = "name"
# WEIGHT = "weight"
# AGE = "age"
# WAR = "WAR"
# PLAYER_PAGE = "url"
#
# # final JSON for participants list not by teams
#
#
#
# # Pulls HTML data (event page) for scraping
# response_event = requests.get(EVENT, verify=False)
# response_event.raise_for_status()
# event_html = response_event.text  # HTML text
# # print(events_html)
# soup_event = BeautifulSoup(event_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping
#
#
# # event HTML url
# participants_href_html = soup_event.find_all(name="div", class_="col s12 m4")[1]("a")
# # print(participants_href_html)
#
#
# #  getting participants URL href no html - list
# participants_url_list = []  # list of URL's
# for body_loop in participants_href_html:
#     limbo = []  # placeholder for participants page url, empties once put in event_hrefs
#     route_num = 0  # used to direct if statements
#     # print(body_loop)
#     if INNER_LOOP_REFERENCE_URL in str(body_loop):  # if "/event" is in body_loop, inner loop executes
#         for anchor_loop in str(body_loop):
#             # print(h)
#             if anchor_loop == "\"":
#                 route_num += 1
#             if route_num == 1:
#                 if anchor_loop == "\"":
#                     pass
#                 else:
#                     limbo.append(anchor_loop)  # adds character to limbo list eg: 'e', 'v', 'e', 'n', 't'
#             if route_num == 2:
#                 combined = "".join(limbo)  # joins characters in limbo to make single str
#                 # print(combined)
#                 participants_url_list.append(combined)  # adds string to events_hrefs then breaks out of loop
#                 break  # and resets limbo for next item
# participants_url_to_str = ""
# for url_to_str in participants_url_list:
#     participants_url_to_str = url_to_str
# participants_final_url = MAIN_SITE_ADDY + participants_url_to_str
# # print(participants_final_url)
# # probably would return this url to def
#
#
# # go to participants list
# # Pulls HTML data (participant page) for scraping
# response_participants = requests.get(participants_final_url, verify=False)
# response_participants.raise_for_status()
# participants_html = response_participants.text  # HTML text
# soup_participants = BeautifulSoup(participants_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping
#
# # iso list data
# iso_participant_data_html = soup_participants.select(selector="tbody tr td")
# # print(iso_participant_data_html)
#
# # creates list of player data from html iso list
# participants_list = {
#
# }
# participant_data_placeholder = []
#
# for p_list_grabber in iso_participant_data_html:
#     participant_data_placeholder.append(p_list_grabber.text)
#
# ret_this_dict = {}
#
# # print(participant_data_placeholder)
# # for x in participant_data_placeholder:
# #     print(x)
#
# part_num = 1
# route_num = 0
# player_placeholder = []
# for x in participant_data_placeholder:
#     if route_num <= 4:
#         player_placeholder.append(x)
#         route_num += 1
#         if route_num == 5:
#             # create dict_obj
#             player_id = player_placeholder[0]
#             name_before = player_placeholder[1]
#             name = name_before.replace(" ", "-")
#             weight = player_placeholder[2]
#             age = player_placeholder[3]
#             war = player_placeholder[4]
#             url = f"/{player_id}/{name}"
#             ret_this_dict[part_num] = {ID: player_id, NAME: name, WEIGHT: weight, AGE: age, WAR: war,
#                                        PLAYER_PAGE: url}
#             part_num += 1
#             route_num = 0
#             player_placeholder = []
#
# print(ret_this_dict)

# create dictionary from data
# for p_data_loop in participant_data_list:
#     print(z)




# with open(file="docs/references/participants_html.html", mode="w") as file:
#     file.write(participants_html)








#  *************************************************************************************************************






# gets tems for players

MAIN_SITE_ADDY = "https://test.wrestlingrating.com/player"


class Player:

    def __init__(self, player_info):
        self.team = self.start(player_info)

    def start(self, player_url):
        # Pulls HTML data (event page) for scraping
        response_event = requests.get(MAIN_SITE_ADDY + player_url, verify=False)
        response_event.raise_for_status()
        player_html = response_event.text  # HTML text
        # print(player_html)
        soup_event = BeautifulSoup(player_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping
        play = soup_event.find(name="p", class_="card-text").text
        # print(play)
        team_list = []
        limbo = []
        for x in play:
            limbo.append(x)
            if x == "\n":
                together = "".join(limbo)
                team_list.append(together.strip())
                limbo = []

        team_name = []

        for t in team_list:
            if "Team" in t:
                print(t[6:])
        return team_name


# start("/670/Gray-Fox-Portella")
