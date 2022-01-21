from bs4 import BeautifulSoup
import requests


# events and dates = https://test.wrestlingrating.com/events/

events_list = []

response_events = requests.get("https://test.wrestlingrating.com/events/", verify=False)
response_events.raise_for_status()
events_html = response_events.text
# print(events_html)

soup_events = BeautifulSoup(events_html, "html.parser")
href_list = []
select_events = soup_events.select(selector="p tbody tr td")

# print(select_events.get("href"))



# listy = []
# for x in select_events:
#     x = x.text.strip("\n")
#     listy.append(x)
#     # print(x)
# print(listy)
# for y in listy:
#     try:
#         int(y)
#     except ValueError:
#         print(y)
#     else:
#         pass




# event page for a specific event (the demonstration event)
#   pool weight range (at the top), the pairing pool, the link to the participant's list,
#   and the on deck matches for each mat = https://test.wrestlingrating.com/event/174/demonstration-event/      (this is just a sample)

# participants page for (the demonstration event),
#   wrestlers weights, ages, and WAR (weight adjusted ratings). = https://test.wrestlingrating.com/event/174/participants/

# rankings page, lists every wrestler in our database along with their team names = https://test.wrestlingrating.com/rankings/