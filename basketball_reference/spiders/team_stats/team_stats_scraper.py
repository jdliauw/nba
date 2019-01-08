from requests_html import HTMLSession
from bs4 import BeautifulSoup

"""
Parsing relevant tables from: 
https://www.basketball-reference.com/leagues/NBA_2019.html
"""

def main():
  # session = HTMLSession()
  # response = session.get("https://www.basketball-reference.com/leagues/NBA_2019.html")
  # response.html.render() # render js

  table_ids = [
    "confs_standings_E",
    "confs_standings_W",
    "team-stats-base",
    "opponent-stats-base",
    "team-stats-per_poss",
    "opponent-stats-per_poss",
    "misc_stats",
    "team_shooting",
    "opponent_shooting",
    # "team-stats-per_game", 
    # "opponent-stats-per_game"
  ]

  for table_id in table_ids:
    # response_html = response.html.find("#{}".format(table_id), first=True).html
    f = open("{}.html".format(table_id), "r")   # DEV
    response_html = f.read()                    # DEV
    soup = BeautifulSoup(response_html, 'html.parser')
    
    if table_id in ["confs_standings_E", "confs_standings_W"]:
      teams = soup.find("table", {"id": "{}".format(table_id)}).find("tbody").findAll("tr")
      conference = "E" if table_id in "confs_standings_E" else "W"
      standings = {conference : {}}

      for team in teams: 
        team_name = team.find("th", {"data-stat": "team_name"}).a["href"].split("/")[2]
        seed = team.find("th", {"data-stat": "team_name"}).text
        seed = int(seed[seed.find("(") + 1 : seed.find(")")])
        standings[conference][team_name] = {"seed": seed}

        fields = team.findAll("td")
        for field in fields:
          data_stat = field["data-stat"]

          # convert to proper type
          val = field.text
          if "." in val:
            val = float(val)
          elif val == "—":
            val = 0.0
          else:
            val = int(val)

          standings[conference][team_name][data_stat] = val

      # for standing in standings:
      #   for team in standings[standing]:
      #     print(team, standings[standing][team])

      # TODO: Store in DB

    elif table_id in ["team-stats-base", "opponent-stats-base", "team-stats-per_poss", "opponent-stats-per_poss"]:
      teams = soup.find("table", {"id": "{}".format(table_id)}).find("tbody").findAll("tr")
      team_stats = { table_id : {}}
      for team in teams:
        team_name = team.find("td", {"data-stat": "team_name"}).a["href"].split("/")[2]

        # if table_id not in 
        rank  = int(team.find("th", {"data-stat" : "ranker"}).text)
        team_stats[table_id][team_name] = {"rank" : rank }
        
        fields = team.findAll("td")
        for field in fields[1:]:
          team_stats[table_id][team_name][field["data-stat"]] = float(field.text) if "." in field.text else int(field.text)

      # for table_id in team_stats:
      #   for team in team_stats[table_id]:
      #     print(team, team_stats[table_id][team])

      # TODO: Store in DB

    elif table_id in ["team_shooting", "opponent_shooting"]:
      teams = soup.find("table", {"id": "{}".format(table_id)}).find("tbody").findAll("tr")
      shooting_stats = {}
      for team in teams:
        team_name = team.find("td", {"data-stat": "team_name"}).a["href"].split("/")[2]

        if team_name not in shooting_stats:
          shooting_stats[team_name] = {}
        
        fields = team.findAll("td")
        for field in fields[1:]:
          shooting_stats[team_name][field["data-stat"]] = float(field.text) if "." in field.text else int(field.text)

    elif table_id == "misc_stats":
      teams = soup.find("table", {"id": "{}".format(table_id)}).find("tbody").findAll("tr")
      misc_stats = {}
      for team in teams:
        team_name = team.find("td", {"data-stat": "team_name"}).a["href"].split("/")[2]

        if team_name not in misc_stats:
          misc_stats[team_name] = {}
        
        fields = team.findAll("td")
        for field in fields[1:]:
          text = field.text
          if field["data-stat"] == "arena_name":
            misc_stats[team_name][field["data-stat"]] = text
            continue

          if field["data-stat"] in ["net_rtg", "attendance", "attendance_per_g"]:
            text = field.text.replace("+", "").replace(",", "")

          misc_stats[team_name][field["data-stat"]] = float(text) if "." in text else int(text)

"""
scraping
controller (2)
message deb/mark
"""

if __name__ == "__main__":
  main()