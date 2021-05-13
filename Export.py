from csv import csv 

class Export():
    def __init__(self,nom):
        self.nom=nom
        

    def export(self,table):
        with open(self.nom, 'w') as f:

            write = csv.writer(f, delimiter = ',')
            write.writerow(table.colonnes)
            write.writerows(table.contenu)
            
            

            
