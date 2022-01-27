from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
                team_name = t[6:]
        return team_name

# start("/670/Gray-Fox-Portella")