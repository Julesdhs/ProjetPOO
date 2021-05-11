from Importcsv import Import 
from TransformationMoyenneglissante import TransformationMoyenneglissante

folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"
t=Import.cree(folder,filename)
t.stringtoint('hosp')
t.stringtoint('rea')
t.stringtoint('rad')
t.stringtoint('dc')


a = TransformationMoyenneglissante(7,['hosp'])
a.transform(t)

folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.cree(folder,filename)
Question1=Pipeline(table)
Question1.ajout_etape(EstimateurSomme('incid_hosp'))
Question1.applique()
