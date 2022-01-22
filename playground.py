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

DATE = "date"
LOCATION = "local"
URL = "url"


json_data = {"events": {
    "demo evnent":
        {"date": "jan. 1, 2020", "location": "over the rainbow", "url": "/event/143"},
    "War Zone local":
        {"date": "may. 23, 2021", "location": "shack", "url": "/event/12"},
    "tourney":
        {"date": "june. 3, 2023", "location": "utah", "url": "/event/105"},
}
             }


json_data["events"]["new event"] = {DATE: "jan 1, 2011", LOCATION: "ohio", URL: "/event/123"}


data_load = json.dumps(json_data, indent=4)
print(data_load)

# with open(file="docs/tests/test_written_events.json", mode="w") as file:
#     json.dump(json_data, file, indent=4)
