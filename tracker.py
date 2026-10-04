import csv

with open("data/tourism.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)

    for index, row in enumerate(reader):
            if index >= 4 and index < 85 :
                  print(row[1], row[8])