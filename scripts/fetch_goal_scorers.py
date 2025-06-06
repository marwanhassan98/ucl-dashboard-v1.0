import requests
import pandas as pd
import os

# Your API token here
API_TOKEN = "f08c6677ff494022ad5195cda5c137ee"
HEADERS = {"X-Auth-Token": API_TOKEN}

# Champions League competition ID is 2001
url = "https://api.football-data.org/v4/competitions/2001/scorers"

# Parameters: top 10 scorers for the 2023 season (update season if needed)
params = {
    "limit": 200,
    "season": 2024
}

# Make the API request
response = requests.get(url, headers=HEADERS, params=params)

if response.status_code == 200:
    data = response.json()
    scorers = data.get("scorers", [])

    # Extract relevant info into a list of dictionaries
    players_list = []
    for item in scorers:
        player = item.get("player", {})
        team = item.get("team", {})
        players_list.append({
            "Name": player.get("name"),
            "Goals": item.get("goals"),
            "Team": team.get("name"),
            "Nationality": player.get("nationality")
        })

    # Create and show DataFrame
    df = pd.DataFrame(players_list)
    print(df)

     # Make sure the folder exists
    os.makedirs("data", exist_ok=True)

    # Save to CSV
    df.to_csv("data/top_scorers.csv", index=False)
    print("Top scorers saved to data/top_scorers.csv")

else:
    print("Failed to fetch data. Status code:", response.status_code)
