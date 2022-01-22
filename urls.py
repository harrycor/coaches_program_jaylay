import json
from bs4 import BeautifulSoup
import requests

# Constants
DATE = "date"
LOCATION = "location"
URL = "url"


json_data_dictionary = {
    "events": {

    }
}


# events and dates = https://test.wrestlingrating.com/events/

events_list = []

response_events = requests.get("https://test.wrestlingrating.com/events/", verify=False)
response_events.raise_for_status()
events_html = response_events.text
# print(events_html)

soup_events = BeautifulSoup(events_html, "html.parser")



href_list = []
final_href = []
select_events = soup_events.select(selector="p tbody tr td")

for x in select_events:
    href_list.append(x)

for y in href_list:
    limbo = []
    num = 0
    # print(y)
    for h in str(y):
        if h == "\"":
            num += 1
        if num == 2:
            combined = "".join(limbo)
            # print(combined)
            final_href.append(combined)
            break
        if num == 1:
            if h == "\"":
                pass
            else:
                limbo.append(h)

print(final_href)
# for this in final_href:
#     print(this)





# select_events = soup_events.select(selector="p tbody tr td")

listy = []
event_date_name_local = []
for x in select_events:
    x = x.text.strip("\n")
    listy.append(x)
    # print(x)
# print(listy)
for y in listy:
    try:
        int(y)
    except ValueError:
        event_date_name_local.append(y)
        # print(y)
    else:
        pass

print(event_date_name_local)

event_maker = []    # used to load each events info before added to dict. deleted each loop

marker_event = 0
marker_url = 0
for create in event_date_name_local:
    if marker_event <= 2:
        # print(create)
        # print("*************")
        event_maker.append(create)
        if marker_event == 2:
            try:
                event_maker.append(final_href[marker_url])
                marker_event = 0
                marker_url += 1
                # print(event_maker)
                date_event_maker = event_maker[0]
                event_event_maker = event_maker[1]
                location_event_maker = event_maker[2]
                url_event_maker = event_maker[3]
                json_data_dictionary["events"][event_event_maker] = {DATE: date_event_maker,
                                                                     LOCATION: location_event_maker,
                                                                     URL: url_event_maker}
                event_maker = []
            except:
                pass
        else:
            marker_event += 1

json_event = json.dumps(json_data_dictionary, indent=4)
print(json_event)


with open(file="docs/references/events_data_inactive.json", mode="w") as file:
    json.dump(json_data_dictionary, file, indent=4)

# event page for a specific event (the demonstration event)
#   pool weight range (at the top), the pairing pool, the link to the participant's list,
#   and the on deck matches for each mat = https://test.wrestlingrating.com/event/174/demonstration-event/      (this is just a sample)

# participants page for (the demonstration event),
#   wrestlers weights, ages, and WAR (weight adjusted ratings). = https://test.wrestlingrating.com/event/174/participants/

# rankings page, lists every wrestler in our database along with their team names = https://test.wrestlingrating.com/rankings/