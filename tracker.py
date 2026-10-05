import csv

def main():
    data = load_data("data/tourism.csv")


    year1 = convert_year(data[3][8]) 
    year2 = convert_year(data[3][9])

    #Testing convert_year function
    print("year1:", year1)
    print("year2:", year2)
      
    #Testing clean_number function
    print(clean_number(data[4][8]))
    print(clean_number(data[4][9]))

    #Printing only the valid rows
    #   for index, row in enumerate(data):
    #        if 4 <= index < 85:
    #             print(row[1], row[8])

def load_data(filename): #Open and read the csv
    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)
            return list(reader)

    except FileNotFoundError:
        print(f"File Not Found: {filename}")
        return []

def convert_year(year): #Converting Buddhist year to Georgian
     # strip non-digit suffixes like "P"
    digits = ''.join(c for c in year if c.isdigit())
    return int(digits) - 543

def clean_number(value): #Cleaning commas and space then return clean number
    try:
        value = int(str(value).strip().replace(",",""))
        return value
    except ValueError:
        print(f"Value Not Found:{value}")


if __name__ == "__main__":
      main()