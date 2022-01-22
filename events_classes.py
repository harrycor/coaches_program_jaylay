import json
from bs4 import BeautifulSoup
import requests

# TODO maybe reorder the event title, date, location list before creating it for easier iteration during JSON creation

# Constants
EVENTS_URL = "https://test.wrestlingrating.com/events/"
DATE = "date"
LOCATION = "location"
URL = "url"
INNER_LOOP_REFERENCE_URL = "/event/"


# Pulls HTML data for scraping
response = requests.get(EVENTS_URL, verify=False)
response.raise_for_status()
events_html = response.text  # HTML text
# print(events_html)
soup_events = BeautifulSoup(events_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping
tbody_data = soup_events.select(selector="p tbody tr td")    # table data from tbody (events info) (list)
# print(tbody_data)


# URL's list
event_hrefs = []    # list of URL's
for body_loop in tbody_data:
    limbo = []      # placeholder for event url, empties once put in event_hrefs
    route_num = 0         # used to direct if statements
    # print(body_loop)
    if INNER_LOOP_REFERENCE_URL in str(body_loop):     # if "/event" is in body_loop, inner loop executes
        for anchor_loop in str(body_loop):
            # print(h)
            if anchor_loop == "\"":
                route_num += 1
            if route_num == 1:
                if anchor_loop == "\"":
                    pass
                else:
                    limbo.append(anchor_loop)   # adds character to limbo list eg: 'e', 'v', 'e', 'n', 't'
            if route_num == 2:
                combined = "".join(limbo)       # joins characters in limbo to make single str
                # print(combined)
                event_hrefs.append(combined)    # adds string to events_hrefs then breaks out of loop
                break                               # and resets limbo for next item
# print(event_hrefs)


# DATE, EVENT NAME, LOCATION list, there is a REASON it was made separate this way
event_date_name_local = []  # list of event-title, date, location, in that order
# this loop strips HTML
for stripper_loop in tbody_data:
    stripper_loop = stripper_loop.text.strip("\n")  # REASON - no href when 'stripped' - **must strip to isolate event
    try:
        int(stripper_loop)
    except ValueError:
        event_date_name_local.append(stripper_loop)
        # print(y)
    else:
        pass
    # print(stripper_loop)
print(event_date_name_local)


# dictionary data for JSON. uses event-title, date, name, location list, PLUS URL list to compile data
# Data to create JSON
data_dict_for_json = {
    "events": {

    }
}
event_placeholder = []    # used as placeholder to load each events info before adding to dict. emptied each loop around
marker_event = 0        # acts as if router
marker_url = 0
for create in event_date_name_local:
    if marker_event <= 2:
        # print(create)
        # print("*************")
        event_placeholder.append(create)    # adds event-title, date, location to placeholder
        if marker_event == 2:
            if "’" in event_placeholder[2]:     # this removes the "’" for the JSON conversion. else its "u2019". yikes
                # print("HELLO*******")
                apos_remover = event_placeholder[2].replace("’", "\'")
                event_placeholder[2] = apos_remover
                # print(apos_remover)
            try:
                event_placeholder.append(event_hrefs[marker_url])   # adds event URL to placeholder
                marker_event = 0    # resets routing
                marker_url += 1     # ensure correct URL is added to event
                # print(event_maker)

                # sets variables  for dict placement
                date_event_maker = event_placeholder[0]
                event_event_maker = event_placeholder[1]
                location_event_maker = event_placeholder[2]
                url_event_maker = event_placeholder[3]

                # Dictionary for JSON
                data_dict_for_json["events"][event_event_maker] = {DATE: date_event_maker,
                                                                   LOCATION: location_event_maker,
                                                                   URL: url_event_maker}

                event_placeholder = []      # resets placeholder for next event
            except:     # for when event_hrefs index is out of range * change?
                pass
        else:
            marker_event += 1   # increases for routing (2 re-routes it)
print(data_dict_for_json)
# JSON used from dictionary data
json_event = json.dumps(data_dict_for_json, indent=4)
print(json_event)
# print("all good")
