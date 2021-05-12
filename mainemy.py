from Importcsv import Import 
from EstimateurSomme import EstimateurSomme
from Pipeline import Pipeline
folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"
t=Import.cree(folder,filename)
t.stringtoint('hosp')
t.stringtoint('rea')
t.stringtoint('rad')
t.stringtoint('dc')


a = EstimateurSomme('hosp')
EstimateurSomme.somme(t,'hosp')
res=a.fit(t)

folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.cree(folder,filename)
Question1=Pipeline()
Question1.ajoute_etape(EstimateurSomme('incid_hosp'))
res=Question1.run(table)
print(res.contenu)
