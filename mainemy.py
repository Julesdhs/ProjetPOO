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


debut_semaine1=
fin_semaine1=
debut_semaine2=
fin_semaine2=
# Semaine1
Table2=Pippeline(table)
Table2.ajout_etape(TransformationTemporelle(debut_semaine1,fin_semaine1))
Table2.ajout_etape(EstimateurMoyenne('incid_hosp'))
print(Table2.applique()[1].contenu)

# Semaine2
Table3.ajout_etape(TransformationTemporelle(debut_semaine2,fin_semaine2))
Table3.ajout_etape(EstimateurMoyenne('incid_hosp'))
print(Table3.applique()[1].contenu)
