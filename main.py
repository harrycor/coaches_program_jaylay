# using tk starting the UI

import tkinter as tk

# constants
DROPDOWN_PADDING = (15, 15)

# window
window = tk.Tk()
window.title("Coaches Teams")
window.config(padx=50, pady=50)


# this will be info from web scraping
events = [1, 2, 3, 4, 5]
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

window.mainloop()
