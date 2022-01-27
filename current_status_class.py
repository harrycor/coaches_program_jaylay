import json
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


MAIN_SITE = "https://test.wrestlingrating.com/"

CURRENTLY_ON_MAT = "Currently Wrestling on"
ON_DECK = "On deck on"
DOUBLE_DECK = "On double deck on"
TRIPLE_DECK = "On triple deck on"

PAIRING_NUMBER = "in the pairing pool"

RESTING = "Resting/Not Active"


class Live:

    def __init__(self, url, lst=None):
        self.live_info = self.doit(url)
        if lst != None:
            self.live_team = self.team_status(lst, self.live_info)

    def doit(self, player_url):
        # Pulls HTML data (event page) for scraping
        response_event = requests.get(MAIN_SITE + player_url, verify=False)
        response_event.raise_for_status()
        player_html = response_event.text  # HTML text
        # print(player_html)
        soup_event = BeautifulSoup(player_html, "html.parser")  # puts HTML into "BeautifulSoup" for scraping
        pool = soup_event.select(selector="tbody tr td a")
        # print(on_deck)

        paring_pool = []
        pairing_dict = {"in pool": {}}
        pairing_number = 1
        for x in pool:
            paring_pool.append(x.text)
        # print(paring_pool)
        for p in paring_pool:
            pairing_dict["in pool"][p] = f"number {pairing_number} {PAIRING_NUMBER}"
            pairing_number += 1
        # print(pairing_dict)


        on_mat = soup_event.find_all(name="p", class_="card-text")[4].text
        # print(on_mat)

        mats_holder = []
        m_hold = []
        for y in on_mat:
            mats_holder.append(y)
            if y == "\n":
                new = "".join(mats_holder).strip()
                # print(new)
                m_hold.append(new)
                mats_holder = []
        # print(m_hold)

        mats = []
        for t in m_hold:
            if "Mat " in t:
                mats.append(t[:-1:])
            elif " vs " in t:
                mats.append(t)
        # print(mats)

        on_off = True
        mats_2 = []
        for m in mats:
            # print(m)
            if "Mat " in m:
                mats_2.append(m)
            elif " vs " in m:
                mat_holder = []
                router = 0
                for inside in m:
                    if on_off is True:
                        mat_holder.append(inside)
                    if inside == "(" and on_off is True:
                        if router == 0:
                            newbie = "".join(mat_holder)[:-2:]
                            mats_2.append(newbie)
                        if router == 1:
                            newbie = "".join(mat_holder)[5:-2:]
                            mats_2.append(newbie)
                            router = 0
                        mat_holder = []
                        on_off = False
                    if inside == ".":
                        on_off = True
                        router += 1
                    else:
                        pass

        # print(mats_2)

        status_all_before = {}
        mat_num = 0
        deck_ref_num = 0
        num = 0
        for thru_mats in mats_2:
            # print(thru_mats)
            if "Mat " in thru_mats:
                num = 0
                mat_num += 1
                status_all_before[f"Mat {mat_num}"] = {}
            else:
                status_all_before[f"Mat {mat_num}"][thru_mats] = num
                deck_ref_num += 1
                if deck_ref_num == 2:
                    num += 1
                    deck_ref_num = 0
        # print(status_all_before)



        m = 1
        for d in status_all_before:
            # print(d)
            for h, y in status_all_before[d].items():
                # print(h, y)
                if y == 0:
                    status_all_before[d][h] = f"{CURRENTLY_ON_MAT} {d}"
                elif y == 1:
                    status_all_before[d][h] = f"{ON_DECK} {d}"
                elif y == 2:
                    status_all_before[d][h] = f"{DOUBLE_DECK} {d}"
                elif y == 3:
                    status_all_before[d][h] = f"{TRIPLE_DECK} {d}"
                else:
                    status_all_before[d][h] = f"pending"

        # print(status_all_before)

        # print("hey")
        status_all_before["in pool"] = pairing_dict["in pool"]

        # print(status_all_before)
        # status_all_before["on mat"] =
        js = json.dumps(status_all_before, indent=4)
        # print(js)
        return status_all_before

    def team_status(self, team, status):
        # print(team)
        t_m = ""
        t_name = ""
        for pl in team:
            t_name = pl
            t_m = team[pl]
        for g in t_m:
            # print(g)    #   player name
            for st in status:
                # print(st)
                for t in status[st]:
                    # print(t)
                    if t == g:
                        # print(t)
                        # print("hello")
                        # print(status[st][t])    # this is the status
                        team[t_name][g]["status"] = status[st][t]
        # print(team)
        team_org = json.dumps(team, indent=4)
        print(team_org)

            # for p in team[pl]:
            #     # print(p)
            #     # print("hello")# first player in coahes list
            #     for st in status:
            #         for tus in status[st]:
            #             if tus == p:
            #                 print(tus)
            #
            #             # print(status[st][tus])




        # team_list = []
        # limbo = []
        # for x in on_deck:
        #     limbo.append(x)
        #     if x == "a":
        #         together = "".join(limbo)
        #         team_list.append(together.strip())
        #         limbo = []
        # print(team_list)

        # print(play)
        # team_list = []
        # limbo = []
        # # for x in play:
        # #     limbo.append(x)
        # #     if x == "\n":
        # #         together = "".join(limbo)
        # #         team_list.append(together.strip())
        # #         limbo = []
        #
        # team_name = []
        #
        # for t in team_list:
        #     if "Team" in t:
        #         team_name = t[6:]


# url = "/event/174/"
#
# players = {"Who is the Champion of Long Island? #3": {
#           "Dynamic": {
#                "Matt-McDermott": {
#                     "id": "466",
#                     "age": "12 years",
#                     "weight": "63 lbs",
#                     "WAR": "5918.3",
#                     "status": "pending"
#                },
#                "Lukas-Ryan": {
#                     "id": "467",
#                     "age": "11.5 years",
#                     "weight": "54 lbs",
#                     "WAR": "4506.5",
#                     "status": "pending"
#                }
#           },
#           "What?!?!": {
#                "Jackson-Ainsley": {
#                     "id": "465",
#                     "age": "11.6 years",
#                     "weight": "57.2 lbs",
#                     "WAR": "4452.7",
#                     "status": "pending"
#                }
#           },
#           "Elite": {
#                "Dylan-Venet": {
#                     "id": "545",
#                     "age": "12.7 years",
#                     "weight": "55 lbs",
#                     "WAR": "4243.1",
#                     "status": "pending"}}}}


# start(url, players)
