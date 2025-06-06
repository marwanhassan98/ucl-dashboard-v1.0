import requests
import pandas as pd
import os

# Replace this with your actual API token
API_TOKEN = "f08c6677ff494022ad5195cda5c137ee"
HEADERS = {'X-Auth-Token': API_TOKEN}

# URL for Champions League teams (competition ID 2001)
url = "https://api.football-data.org/v4/competitions/2001/teams"

# Request data from API
response = requests.get(url, headers=HEADERS)

# Check if successful
if response.status_code == 200:
    print("✅ Data fetched successfully!")

    data = response.json()
    teams = data.get("teams", [])

    # Extract needed fields
    team_list = []
    for team in teams:
        team_list.append({
            "id": team["id"],
            "name": team["name"],
            "shortName": team["shortName"],
            "tla": team["tla"],  # 3-letter abbreviation
            "area": team["area"]["name"],
            "venue": team["venue"],
            "logo_url": team["crest"]  # This is the image link
        })

    # Create dataframe
    df = pd.DataFrame(team_list)

    # Create 'data/' folder if it doesn't exist
    os.makedirs("../data", exist_ok=True)

    # Save CSV
    
    print("Saving CSV to:", os.path.abspath("data/champions_league_teams.csv"))
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/champions_league_teams.csv", index=False)
    
    df.to_csv("../data/champions_league_teams.csv", index=False)
    print("✅ Saved to champions_league_teams.csv")

else:
    print("❌ Failed to fetch data:", response.status_code)
