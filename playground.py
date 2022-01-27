# import json
# import pandas
#
#
# info = []
#
# data = pandas.read_excel("docs/tests/test_wresters_status.xlsx")
#
# to_json = data.to_json()
# print(to_json)

from bs4 import BeautifulSoup
import requests
import json

# DATE = "date"
# LOCATION = "local"
# URL = "url"
# "Player’s"
# "Player’'';,`~s"
#
# json_data = {"events": {
#     "demo evnent":
#         {"date": "jan. 1, 2020", "location": "over’s the rainbow  ******", "url": "/event/143"},
#     "War Zone local":
#         {"date": "may. 23, 2021", "location": "shack", "url": "/event/12"},
#     "tourney":
#         {"date": "june. 3, 2023", "location": "utah's", "url": "/event/105"},
# }
#              }
#
#
# # json_data["events"]["new event"] = {DATE: "jan 1, 2011", LOCATION: "ohio", URL: "/event/123"}
#
#
# data_load = json.dumps(json_data, indent=4)
# print(data_load)
#
# print()
# print("******")
# print()
#
# this = ["hello", "there", "this isn’t", "okay"]
# for x in this:
#     if "’" in x:
#         print("here")
#         y = x.replace("’", "fixed")
#         print(y)
#         continue
#     else:
#         pass
#     print(x)


# with open(file="docs/tests/test_written_events.json", mode="w") as file:
#     json.dump(json_data, file, indent=4)

# a = ["okay then /event/12/ here", "super/ev", "ghref= \"/event/234/\" tryinghere"]

# this = []
#
# for x in a:
#     limbo = []
#     num = 0
#     if "/event/" in x:
#         print(x)
#         for z in x:
#             if z == "\"":
#                 num += 1
#             if num == 2:
#                 combined = "".join(limbo)
#                 this.append(combined)
#                 break
#             if num == 1 and z != "\"":
#                 limbo.append(z)
#             else:
#                 pass
#         # print(z)
# for h in this:
#     print(h)


participants_and_teams = {
    "demo event name": {
        "data": {"url": "event/000/demo-event-name"},
        "teams": {
            "dynamic": {
                "jim": {
                    "id": 1832,
                    "age": 11,
                    "team": "dynamic",
                    "weight": 152.2,
                    "WAR": 887.3
                },
                "joe": {
                    "id": 432,
                    "age": 15,
                    "team": "dynamic",
                    "weight": 130.2,
                    "WAR": 527.3
                }
            },
            "team cool": {
                "john": {
                    "id": 1832,
                    "age": 11,
                    "team": "team cool",
                    "weight": 152.2,
                    "WAR": 887.3
                },
                "mike": {
                    "id": 432,
                    "age": 15,
                    "team": "team cool",
                    "weight": 130.2,
                    "WAR": 527.3
                }
            }
        },

    },
}

# with open(file="docs/tests/test_participants.json", mode="w") as file:
#     json.dump(participants_and_teams, file, indent=6)
if "team cool" in participants_and_teams["demo event name"]["teams"]:
    print("yes")
else:
    print("no")

scrape_from_participants_list = {
    "participants": {
        1: {
            "id": 1385,
            "name": "devin mcribb",
            "weight": "273 lbs",
            "age": 19,
            "WAR": 12260,
            "wrestlers url": "/1385/player"
        },
        2: {
            "id": 32,
            "name": "broseph",
            "weight": "999 lbs",
            "age": 112,
            "WAR": 321,
            "wrestlers url": "sly"
        }
    }
}

# for x in scrape_from_participants_list["participants"]:
#     print(x)
# with open(file="docs/tests/participants_page_grab_ex.json", mode="w") as file:
#     json.dump(scrape_from_participants_list, file, indent=6)

# hey = "h%el%lo"
#
# a = hey.replace("%", "")
# print(a)

# print("/")


testing = {"dynamic": {
    "jim": {
        "id": 1832,
        "age": 11,
        "team": "dynamic",
        "weight": 152.2,
        "WAR": 887.3
    },
    "joe": {
        "id": 432,
        "age": 15,
        "team": "dynamic",
        "weight": 130.2,
        "WAR": 527.3
    }}}

testing["dynamic"] = {"bill": {"id": 123, "war": 1233, "team": "cool"}}
print(testing)
