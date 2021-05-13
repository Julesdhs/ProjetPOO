from Importcsv import Import
from EstimateurSomme import EstimateurSomme
from Pipeline import Pipeline
import os


## Question 1): Quel est le nombre total d'hospitalisation dues au covid-19?
#on crée la table
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)
#on crée la pipeline
Question1=Pipeline(table)
Question1.ajout_etape(EstimateurSomme('incid_hosp'))
res1=Question1.applique()
#on retourne le résultat
print("le nombre total d'hospitalisations':")
print(res1[0].contenu)

## Question 2) Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département?
#on crée la table
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('incid_hosp')
#on crée la pipeline
today = '2021-03-03'
Question2=Pipeline(table)
Question2.ajout_etape(TransformationTemporelle('2021-02-25','2021-03-03'))
Question2.applique()
#on fait des modifications pour obtenir la somme par departements
tabledep=Import.creecsv(folder,filename)
TransformationSelectionVariables(['dep']).transform(tabledep)
tableres = Table(['dep'],tabledep.contenu[0:101])
indhosp = table.colonnes.index('incid_hosp')
inddep = table.colonnes.index('dep')
col = [0 for k in range(101)]
for ligne in table.contenu:
    indice = tableres.contenu.index([ligne[inddep]])
    col[indice]+= ligne[indhosp]
tableres.ajoutcol('nouv_hosp_hebdo',col)
print("le tableau de résultat:")
print(tableres.contenu)

#on exporte le tableau dans le dossier où sont les données
os.chdir(folder)
tableres.export('tableres.csv')




##Question 3) Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à celle de la semaine dernière?
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)
# Semaine1
debut_semaine1='2021-02-18'
fin_semaine1='2021-02-24'



pip2=Pipeline(table)
pip2.ajout_etape(TransformationTemporelle(debut_semaine1,fin_semaine1))
res2 = pip2.applique()
pip2.ajout_etape(EstimateurMoyenne('incid_hosp'))
res2=pip2.applique()
print("le résultat pour la semaine dernière :")
print(res2[0].contenu)
#on trouve 13,57


# Semaine2
debut_semaine2='2021-02-25'
fin_semaine2='2021-03-03'
table=Import.creecsv(folder,filename)

Table3=Pipeline(table)
Table3.ajout_etape(TransformationTemporelle(debut_semaine2,fin_semaine2))
res3 = Table3.applique()
Table3.ajout_etape(EstimateurMoyenne('incid_hosp'))
res3=Table3.applique()
print("le résultat pour cette semaine :")
print(res3[0].contenu)
#on trouve 13.49

##Question 4)Quel est le résultat de k-means avec k = 3 sur les données des départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours?
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)
pip4 = Pipeline(table)
pip4.ajout_etape(TransformationTemporelle('2021-01-01','2021-01-31'))
res4 = pip4.applique()
pip4.ajout_etape(EstimateurKmeans(3,['incid_hosp','incid_rea','incid_dc','incid_rad']))
res4 = pip4.applique()
print(res4[0].contenu)


##5)Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?












