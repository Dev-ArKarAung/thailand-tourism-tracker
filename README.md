# Thailand Tourism Tracker

## Overview
A Python project that processes Thailand tourism data from the Ministry of Tourism and Sports. It cleans visitor figures, translates Thai province names into English, and calculates tourism statistics for 2024 and 2025.

## Features
- Load and process CSV data
- Convert Buddhist calendar years to Gregorian years
- Clean visitor-count values
- Filter province-level records and exclude regional summaries
- Translate Thai province names into English
- Calculate total visitors and year-over-year percentage change
- Identify provinces with the highest and lowest visitor counts
- Export cleaned province-level data to CSV

## Technologies
- Python
- CSV module
- Git and GitHub

## How to Run
1. Clone or download this repository.
2. Ensure the raw dataset is located at `data/tourism.csv`.
3. Run:
   `python tracker.py`
4. View the results in the terminal and open `output/tourism_summary.csv`.

## Output
The generated CSV contains the English province name, visitor counts for 2025 and 2024, and the percentage change for each province.

## Data Source

Thailand Ministry of Tourism and Sports — [Thailand tourism visitor data](https://data.go.th/dataset/number_of_visitors).

## Limitations

The current version is designed around the structure of the supplied CSV file and its 2025 and 2024 visitor columns.