import json
import events_classes
import participants_class
import team_get_class

import tkinter as tk

# CONSTANTS
ID = "id"
NAME = "name"
WEIGHT = "weight"
AGE = "age"
WAR = "WAR"
PLAYER_PAGE = "url"
TEAM = "team"

# Tkinter
DROPDOWN_PADDING = (15, 15)

# Events data
events_data = events_classes.EventsData()
events_url = json.loads(events_data.json_file)
# print(events_url)

# creates list for dropdown in tkinter
list_of_events = []
for x in events_url["events"]:
    list_of_events.append(x)
# print(list_of_events)
t_for_c = {}
e_name = ""


def url():
    global t_for_c
    global e_name
    site = clicked_events.get()
    e_name = site
    teams_for_coaches = {site: {}}
    # print(site)
    url_to_send = events_url["events"][site]["url"]
    participants_list_gather = participants_class.ParticipantsInfoForSend(url_to_send)
    list_ret = participants_list_gather.participants_list_event
    # print(list_ret)
    for t in list_ret:
        to_send = list_ret[t]["url"]
        # print(t)
        #     print(to_send)
        team_req = team_get_class.Player(to_send)  # class created each loop
        # print(team_req.team)
        team_name = team_req.team
        # print(team_name)

        name = list_ret[t][NAME]
        player_id = list_ret[t][ID]
        age = list_ret[t][AGE]
        weight = list_ret[t][WEIGHT]
        war = list_ret[t][WAR]
        try:
            teams_for_coaches[site][team_name][name] = {
                    ID: player_id,
                    AGE: age,
                    WEIGHT: weight,
                    WAR: war,
                    "status": "pending"
                }
        except KeyError:
            teams_for_coaches[site][team_name] = {name: {
                    ID: player_id,
                    AGE: age,
                    WEIGHT: weight,
                    WAR: war,
                    "status": "pending"
                }}

    # print(teams_for_coaches)
    new_teams = []
    for h in teams_for_coaches[site]:
        new_teams.append(h)
    clicked_teams.set("select team")
    drop_teams = tk.OptionMenu(window, clicked_teams, *new_teams)
    drop_teams.grid(row=0, column=1, padx=DROPDOWN_PADDING)
    j_dump = json.dumps(teams_for_coaches, indent=5)
    print(j_dump)
    t_for_c = teams_for_coaches
# for x in events_url["events"]:
#     for y in events_url["events"][x]:
#         print(y)

# participants_data = participants_class.Participants_info_for_send(events_data.json_file[])


def check_status():
    global t_for_c
    team_select = clicked_teams.get()
    for x in t_for_c[e_name]:
        if x == team_select:
            coaches_rev = {team_select: t_for_c[e_name][x]}
            coaches_new = json.dumps(coaches_rev, indent=4)
            print(coaches_new)



# # TKINTER. most ikely will NOT be used. this is a good reference for operation
# window
window = tk.Tk()
window.title("Coaches Teams")
window.config(padx=50, pady=50)

# this will be info from web scraping
events = list_of_events
teams = ["dynamic", "team 10", "team 20", "team 30", "team 40"]

# Dropdowns
# events *
clicked_events = tk.StringVar()
clicked_events.set("select events")
drop_events = tk.OptionMenu(window, clicked_events, *events)
drop_events.grid(row=0, column=0, pady=DROPDOWN_PADDING)

# teams *
clicked_teams = tk.StringVar()
clicked_teams.set("select team")
drop_teams = tk.OptionMenu(window, clicked_teams, *teams)
drop_teams.grid(row=0, column=1, padx=DROPDOWN_PADDING)

# Buttons
# event render
events_button = tk.Button(text="Find Participants", command=url)
events_button.grid(row=1, column=0)

# team button
team_button = tk.Button(text="team status", command=check_status)
team_button.grid(row=1, column=1)

window.mainloop()
