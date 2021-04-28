import csv

# Dossier où se trouve le fichier :
folder = ''
filename = 'covid-hospit-incid-reg-2021-03-03-17h20.csv'
data = []
with open(folder + filename, encoding='ISO-8859-1') as csvfile :
covidreader = csv.reader(csvfile, delimiter=' ;')
for row in covidreader :
    data.append(row)