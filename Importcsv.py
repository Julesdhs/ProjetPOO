import csv as csv
import json

class Import():

    @staticmethod
    def creecsv(fichier,nom):
        data = []

        with open(fichier + nom, encoding ='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter=';')
            for row in covidreader :
                data.append(row)

        return(Table(data[0], [data[k] for k in range(1,len(data))]))

    def creejson(fichier,nom):

        with open(fichier + nom) as json_file :
            data = json.load(json_file)

        Lt=[]
        for key1 in data:
            t=Table()
            for k in range(len(data[key1])):
                ligne=[]
                for key2 in data[key1][k]:
                    if key2 not in t.colonnes :
                        t.colonnes.append(key2)
                    ligne.append(data[key1][k][key2])
                t.ajoutlig(ligne)
            Lt.append(t)
        return(Lt)