import csv
import json

def csv_to_json(csv1,csv2,csv3,json1):
    jsonArray = []
    hex1 = "rgb(255,0 , 0)"
    hex2 = "rgb(0, 255, 0)"
    hex3 = "rgb(0, 0, 255)"
    hex4 = "rgb(0, 255, 255)"
    hex5 = "rgb(255, 0, 255)"
    hex6 = "rgb(255, 255, 0)"
    hex7 = "rgb(0, 0, 0)"


# odczyt pliku
    with open(csv1, encoding='utf-8') as csvf:
        # zaladowanie pliku csv
        csvReader = csv.DictReader(csvf)
# konwersja csv do slownika pythona
        for row in csvReader:
            # dodanie do slownika
            jsonArray.append(row)
    jsonArray.append(hex1)
    jsonArray.append(hex2)
    jsonArray.append(hex3)

    with open(csv2, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)

    jsonArray.append(hex4)
    jsonArray.append(hex5)
    jsonArray.append(hex6)

    with open(csv3, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
    jsonArray.append(hex7)
    with open(json1, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
# pliki
csv1 = r'example.csv'
csv2 = r'example1.csv'
csv3 = r'example2.csv'
json1 = r'output.json'
csv_to_json(csv1,csv2,csv3,json1)

