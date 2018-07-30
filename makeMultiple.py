import csv
import json

print('--- loading data ---')

files = ['06_07.csv', '07_08.csv', '09_10.csv', '10_11.csv', '11_12.csv', '12_13.csv', '13_14.csv', '14_15.csv', '15_16.csv', '16_17.csv']

for entry in files:
    csv_file = open(entry)
    header = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST',
              'AST',
              'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']
    #csv_reader = csv.DictReader(csv_file, header)
    print(entry)


'''    
csv_file = open("06_07.csv", "r")
header = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST',
          'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']
csv_reader = csv.DictReader(csv_file, header)

saison_06_07 = []

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
    saison_06_07.append(dic)

bundesliga = {
    'saison_06_07' : saison_06_07
}

print(bundesliga) # läuft!

print("--- writing to file ---")

# Ausgabe als JSON
with open('saison_06_07.json', 'w', encoding='utf-8') as json_file:
    json.dump(bundesliga, json_file, indent=2)

print("--- finished ---")
'''