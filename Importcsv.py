import csv as csv

class Import():

    @staticmethod
    def cree(fichier,nom):
        data = []

        with open(fichier + nom, encoding ='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter=';')
            for row in covidreader :
                data.append(row)

        return(Table(data[0], [data[k] for k in range(1,len(data))]))

