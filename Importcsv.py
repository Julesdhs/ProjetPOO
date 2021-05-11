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


        with open(folder + filename) as json_file :
            data = json.load(json_file)

        return(Table(data[0], [data[k] for k in range(1,len(data))]))