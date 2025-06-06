import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file contents into environment variables

API_TOKEN = os.getenv("API_TOKEN")

HEADERS = {'X-Auth-Token': API_TOKEN}

TEAM_DETAIL_URL = "https://api.football-data.org/v4/teams/{}"

def fetch_players():
    # Read teams CSV
    teams_df = pd.read_csv("data/champions_league_teams.csv")
    all_players = []

    for _, row in teams_df.iterrows():
        team_id = row["id"]
        team_name = row["name"]
        print(f"Fetching players for {team_name} (ID: {team_id})")

        url = TEAM_DETAIL_URL.format(team_id)
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Failed to fetch players for {team_name}")
            continue

        data = response.json()
        squad = data.get("squad", [])

        for player in squad:
            all_players.append({
                "team": team_name,
                "player_name": player.get("name"),
                "position": player.get("position"),
                "nationality": player.get("nationality"),
                "dateOfBirth": player.get("dateOfBirth"),
                "shirtNumber": player.get("shirtNumber"),
            })

    # Create DataFrame and save CSV
    df = pd.DataFrame(all_players)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/champions_league_players.csv", index=False)
    print("✅ Players data saved to data/champions_league_players.csv")

if __name__ == "__main__":
    fetch_players()
