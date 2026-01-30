import pandas as pd
import json

files = {
    "batting": "t20_wc_batting_summary.json",
    "bowling": "t20_wc_bowling_summary.json",
    "matches": "t20_wc_match_results.json",
    "players": "t20_wc_player_info.json"
}

# Dictionary to store DataFrames
dfs = {}

# 1. Process Batting Summary
with open(files['batting']) as f:
    data = json.load(f)
    all_records = []
    for match in data:
        all_records.extend(match['battingSummary'])
    dfs['Batting_Summary'] = pd.DataFrame(all_records)

# 2. Process Bowling Summary
with open(files['bowling']) as f:
    data = json.load(f)
    all_records = []
    for match in data:
        all_records.extend(match['bowlingSummary'])
    dfs['Bowling_Summary'] = pd.DataFrame(all_records)

# 3. Process Match Results
with open(files['matches']) as f:
    data = json.load(f)
    dfs['Match_Results'] = pd.DataFrame(data[0]['matchSummary'])

# 4. Process Player Info
dfs['Player_Info'] = pd.read_json(files['players'])

# Export to a single Excel file with multiple sheets
with pd.ExcelWriter('T20_World_Cup_Data.xlsx') as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Conversion and merge complete! File saved as T20_World_Cup_Data.xlsx")