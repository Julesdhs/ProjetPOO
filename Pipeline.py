#from OperationAbstraite import OperationAbstraite

class Pipeline():
    def __init__(self,table,pile = None,res = None) :
        self.table = table
        if pile is None:
            pile = []
        if res is None :
            res = []
        self.pile = pile
        self.res = res

    def ajout_etape(self,operation):
        self.pile.append(operation)

    def applique(self):
        for k in range(len(self.pile)):
                self.res.append(self.pile[k].process(self.table))
        return(self.res)

        ##
class Pipeline():
    def __init__(self):
        self.operations=[]

    def ajout_etape(self,etape):
        self.operations.append(etape)

    def applique(self,table):
        res=[]
        for etape in self.operations:
            res.append(etape.process(table))
        return(res)



folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('incid_hosp')

# Semaine1

debut_semaine1='2021-02-18'
fin_semaine1='2021-02-24'

pip2=Pipeline()
pip2.ajout_etape(TransformationTemporelle(debut_semaine1,fin_semaine1))
pip2.ajout_etape(EstimateurMoyenne('incid_hosp'))
res2=pip2.applique(table)
res2[-1].contenu
