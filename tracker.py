import csv
from translations import province_names

def main():
    data = load_data("data/tourism.csv")

    if len(data) <= 3:
        print("Error")
        return
    
    year1 = convert_year(data[3][8])
    year2 = convert_year(data[3][9])

    regions = ["ภาคกลาง",
    "ภาคตะวันออก",
    "ภาคใต้",
    "ภาคเหนือ"]

    province_data = prepare_province_data(data, regions)
    stats = calculate_stats(province_data)
    total_2025, total_2024, percentage_change, highest_visitors, highest_province, lowest_visitors, lowest_province = stats

    save_summary(province_data, "output/tourism_summary.csv")

    print(f"Total visitors in {year1}: {total_2025:,}")
    print(f"Total visitors in {year2}: {total_2024:,}")
    print(f"Percentage change:{percentage_change:.2f}%")
    print(f"Highest: {highest_province} - {highest_visitors:,}")
    print(f"Lowest: {lowest_province} - {lowest_visitors:,}")
    
def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)
            return list(reader)

    except FileNotFoundError:
        print(f"File Not Found: {filename}")
        return []

def convert_year(year):
    digits = ''.join(c for c in year if c.isdigit())
    return int(digits) - 543

def clean_number(value): 
    try:
        value = int(str(value).strip().replace(",",""))
        return value
    except ValueError:
        print(f"Value Not Found:{value}")
        return 0

def translate_province(thai_name):
    return province_names.get(thai_name, thai_name)

def prepare_province_data(data, regions):
    province_data = []

    for index, row in enumerate(data):
        if 4<= index < 85 and row[1] not in regions:
            province = translate_province(row[1])
            visitor_2025 = clean_number(row[8])
            visitor_2024 = clean_number(row[9])

            percentage_change = ((visitor_2025 - visitor_2024)/visitor_2024)* 100

            province_data.append({
                "province": province,
                "2025": visitor_2025,
                "2024": visitor_2024,
                "Change": percentage_change
            })

    return province_data

def calculate_stats(province_data):
    total_2025 = 0
    total_2024 = 0
    highest_visitors = 0
    highest_province = ""
    lowest_visitors = float('inf')
    lowest_province = ""

    for item in province_data:
        total_2025 += item["2025"]
        total_2024 += item["2024"]

        if item["2025"] > highest_visitors:
            highest_visitors = item["2025"]
            highest_province = item["province"]

        if item["2025"] < lowest_visitors:
            lowest_visitors = item["2025"]
            lowest_province = item["province"]

    percentage_change = ((total_2025 - total_2024) / total_2024) * 100 if total_2024 else 0

    return (
        total_2025, total_2024,
        percentage_change,
        highest_visitors, highest_province,
        lowest_visitors, lowest_province
    )

def save_summary(province_data, filename):
    with open(filename, "w", encoding= "utf-8", newline="") as file:
        fieldnames = ["province", "2025", "2024", "Change"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(province_data)

if __name__ == "__main__":
      main()