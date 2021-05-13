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

   # Question 3 Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à celle de la semaine dernière ?
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
