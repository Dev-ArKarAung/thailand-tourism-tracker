import csv
from translations import province_names

def main():
    data = load_data("data/tourism.csv")

    year1 = convert_year(data[3][8]) #2568P to 2025
    year2 = convert_year(data[3][9]) #2567 to 2024

    #List to exclude unrelated rows
    regions = ["ภาคกลาง",
    "ภาคตะวันออก",
    "ภาคใต้",
    "ภาคเหนือ"]

    stats = calculate_stats(data, regions)
    total_2025, total_2024, percentage_change, highest_visitors, highest_province, lowest_visitors, lowest_province = stats

    print(f"Total visitors in {year1}: {total_2025:,}")
    print(f"Total visitors in {year2}: {total_2024:,}")
    print(f"Percentage change: {percentage_change:.2f}%")
    print(f"Highest: {highest_province} - {highest_visitors:,}")
    print(f"Lowest: {lowest_province} - {lowest_visitors:,}")
    

def load_data(filename): #Open and read the csv
    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)
            return list(reader)

    except FileNotFoundError:
        print(f"File Not Found: {filename}")
        return []

def convert_year(year): #Converting Buddhist year to Gregorian
     # strip non-digit suffixes like "P"
    digits = ''.join(c for c in year if c.isdigit())
    return int(digits) - 543

def clean_number(value): #Cleaning commas and space then return clean number
    try:
        value = int(str(value).strip().replace(",",""))
        return value
    except ValueError:
        print(f"Value Not Found:{value}")
        return 0

def translate_province(thai_name):
    return province_names.get(thai_name, thai_name)

def calculate_stats(data, regions):
    total_2025 = 0
    total_2024 = 0
    highest_visitors = 0
    highest_province = ""
    lowest_visitors = float('inf')
    lowest_province = ""

    for index, row in enumerate(data):
            if 4 <= index < 85 and row[1] not in regions:
                province = translate_province(row[1])
                visitor_2025 = clean_number(row[8])
                visitor_2024 = clean_number(row[9])
    
                #finding out the total visitors for 2025 and 2024
                total_2025 += visitor_2025
                total_2024 += visitor_2024
    
                #Finding out which province has the highest visitors in 2025
                if visitor_2025 > highest_visitors:
                    highest_visitors = visitor_2025
                    highest_province = province
    
                #Finding out which province has the lowest visitors in 2025
                if visitor_2025 < lowest_visitors:
                    lowest_visitors = visitor_2025
                    lowest_province = province

    #Finding out how much percentage of visitors change from 2024 to 2025
    percentage_change = ((total_2025 - total_2024)/total_2024)*100

    return ( 
        total_2025, total_2024,
        percentage_change,
        highest_visitors, highest_province,
        lowest_visitors, lowest_province
        )

if __name__ == "__main__":
      main()