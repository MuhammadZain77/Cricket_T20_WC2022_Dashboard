# Cricket_T20_WC2022_Dashboard


Cricket T20 World Cup 2022 Analytics Dashboard (Power BI)

📌 Project Overview:

This project is an end-to-end Cricket T20 World Cup 2022 Analytics Dashboard built using Python, Excel, and Power BI.
The goal of this project is to transform raw cricket data into meaningful insights through data engineering, data cleaning, data modeling, and interactive visualization.

The dashboard provides deep insights into:

Batting performance

Bowling performance

Match results

Player statistics

Team-wise analysis

This project demonstrates the complete data analytics workflow from raw JSON files to an interactive Power BI dashboard.

🎯 Objectives:

Convert raw cricket data into structured datasets

Perform data cleaning and transformation

Build relationships between multiple tables

Create meaningful KPIs using DAX

Design an interactive and visually appealing dashboard

Provide actionable cricket insights

🗂️ Data Source

Initially, the data was available in JSON format containing:

Match results

Batting statistics

Bowling statistics

Player information

🔄 Data Processing Pipeline
1️⃣ JSON → Excel (Python & Pandas)

Parsed multiple JSON files using Python

Extracted relevant fields

Merged multiple datasets into a single Excel file

Used Pandas functions for data manipulation

Key Python Operations:

Reading JSON files

Normalizing nested JSON data

Merging datasets

Exporting to Excel

2️⃣ Data Cleaning & Transformation (Power BI)

Performed the following transformations in Power BI:

Removed duplicate records

Handled missing and null values

Changed data types

Standardized column names

Created calculated columns

Filtered irrelevant data

Prepared fact and dimension tables

3️⃣ Data Modeling (Power BI)

Created relationships between tables

Defined cardinalities (One-to-Many, Many-to-One)

Built a star-schema-like model

Ensured slicers and visuals work correctly

🧮 DAX Measures & KPIs

Created multiple DAX measures to generate insights, including:

📊 Batting Metrics

Total Runs Scored

Average Strike Rate

Batting Average

Total Fours & Sixes

Top Run Scorers

Most Sixes by Batsman

🎯 Bowling Metrics

Total Wickets

Average Economy Rate

Bowling Strike Rate

Most Wickets by Bowler

Most Economical Bowlers

Overs Bowled

🏆 Match & Team Metrics

Total Matches

Team-wise Runs

Team-wise Wickets

Match Results Overview

📈 Dashboard Features

The Power BI dashboard consists of multiple interactive pages:

🥇 Batting Stats Dashboard

Top run scorers

Batting averages

Most sixes and fours

Team-wise batting performance

🎯 Bowling Stats Dashboard

Top wicket takers

Economy rate analysis

Overs bowled

Team-wise bowling performance

🏆 Match Results Overview

Match outcomes

Team comparisons

Tournament summary

👤 Player Performance Dashboard

Individual player statistics

Comparative analysis

⚙️ Interactive Features

Dynamic slicers

Filters by player, team, match, etc.

Drill-down analysis

Responsive visuals

🛠️ Tools & Technologies Used
Category	Tools
Programming Language	Python (Pandas)
Data Format	JSON, Excel
BI Tool	Power BI
Data Modeling	Relationships & Cardinalities
Analytics	DAX
Visualization	Power BI Charts & KPIs
Version Control	Git & GitHub

📂 Project Structure
Cricket_T20_WC2022_Dashboard/
│
├── Batting_Stats.png
├── Bowling_Stats.png
├── Match_Results_Overview.png
├── Player_Performance.png
│
├── T20_World_Cup_Data.xlsx
├── Merge_Excel_Format.py
│
├── t20_wc_batting_summary.json
├── t20_wc_bowling_summary.json
├── t20_wc_match_results.json
├── t20_wc_player_info.json
│
└── README.md

🚀 Key Insights from Dashboard

Identification of top-performing batsmen and bowlers

Comparison of team performances

Analysis of economy and strike rates

Detection of impactful players in the tournament

Team dominance in batting and bowling

💡 Learning Outcomes

Through this project, I gained hands-on experience in:

Real-world data cleaning and transformation

JSON data handling using Python

Data modeling in Power BI

Writing optimized DAX measures

Dashboard design and storytelling with data

End-to-end analytics workflow

📷 Dashboard Preview

(Screenshots available in the repository)

📌 Future Improvements

Add predictive analytics using Python/ML

Integrate real-time cricket APIs

Add more advanced DAX measures

Improve UI/UX design with advanced themes

Create player comparison and ranking system

👨‍💻 Author

Muhammad Zain
Data Analytics & Power BI Enthusiast

📌 GitHub: (https://github.com/MuhammadZain77)
📌 LinkedIn: (https://www.linkedin.com/in/mohammad-zain77/)

⭐ If you like this project, give it a star!
