import csv
import json

print('--- loading data ---')

csv_file = open("16_17.csv", "r")
header = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST',
          'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']
csv_reader = csv.DictReader(csv_file, header)

saison_16_17 = []

print('--- processing data ---')
for row in csv_reader:
    dic = {}
    dic['Div'] = row['Div']
    dic['Date'] = row['Date']
    dic['HomeTeam'] = row['HomeTeam']
    dic['AwayTeam'] = row['AwayTeam']
    dic['FTHG'] = row['FTHG']
    dic['FTAG'] = row['FTAG']
    dic['FTR'] = row['FTR']
    dic['HTHG'] = row['HTHG']
    dic['HTAG'] = row['HTAG']
    dic['HTR'] = row['HTR']
    dic['HS'] = row['HS']
    dic['AS'] = row['AS']
    dic['HST'] = row['HST']
    dic['AST'] = row['AST']
    dic['HF'] = row['HF']
    dic['AF'] = row['AF']
    dic['HC'] = row['HC']
    dic['AC'] = row['AC']
    dic['HY'] = row['HY']
    dic['AY'] = row['AY']
    dic['HR'] = row['HR']
    dic['AR'] = row['AR']
    saison_16_17.append(dic)

bundesliga = {
    'saison_16_17': saison_16_17
}

print(bundesliga) # läuft!

print("--- writing to file ---")

# Ausgabe als JSON
with open('saison_16_17.json', 'w', encoding='utf-8') as json_file:
    json.dump(bundesliga, json_file, indent=2)

print("--- finished ---")
