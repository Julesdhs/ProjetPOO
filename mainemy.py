from Importcsv import Import
from EstimateurSomme import EstimateurSomme
from Pipeline import Pipeline
import os

folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"



## Question 1): Quel est le nombre total d'hospitalisation dues au covid-19?
#on crée la table
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
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
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('incid_hosp')
#on crée la pipeline
Question2=Pipeline(table)
Question2.ajout_etape(TransformationTemporelle('2021-05-05','2021-05-12'))
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
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
# Semaine1
debut_semaine1='2021-04-28'
fin_semaine1='2021-05-04'



pip2=Pipeline(table)
pip2.ajout_etape(TransformationTemporelle(debut_semaine1,fin_semaine1))
res2 = pip2.applique()
pip2.ajout_etape(EstimateurMoyenne('incid_hosp'))
res2=pip2.applique()
print("le résultat pour la semaine dernière :")
print(res2[0].contenu)
#on trouve 14,11


# Semaine2
debut_semaine2='2021-05-05'
fin_semaine2='2021-05-12'
table=Import.creecsv(folder,filename)

Table3=Pipeline(table)
Table3.ajout_etape(TransformationTemporelle(debut_semaine2,fin_semaine2))
res3 = Table3.applique()
Table3.ajout_etape(EstimateurMoyenne('incid_hosp'))
res3=Table3.applique()
print("le résultat pour cette semaine :")
print(res3[0].contenu)
#on trouve 10,46

##Question 4)Quel est le résultat de k-means avec k = 3 sur les données des départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours?
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
pip4 = Pipeline(table)
pip4.ajout_etape(TransformationTemporelle('2021-01-01','2021-01-31'))
res4 = pip4.applique()
pip4.ajout_etape(EstimateurKmeans(3,['incid_hosp','incid_rea','incid_dc','incid_rad']))
res4 = pip4.applique()


##Question 5)Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?

## Question 6) Quel est le nombre de décès(à l'hopital)totaux à ce jour et selon les sexes?
#on crée la table
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('dc')
pip6 = Pipeline(table)
pip6.ajout_etape(TransformationSelectionVariables(['dep','sexe','jour','dc']))
res6 = pip6.applique()
pip6.ajout_etape(TransformationTemporelle('2021-05-12','2021-05-12'))
res6 = pip6.applique()
pip6.ajout_etape(TransformationSpatiale(1,0))
res6 = pip6.applique()

#on exporte le tableau dans le dossier où sont les données
os.chdir(folder)
table.export('question6.csv')

## Question 7) Quel est le nombre de services hospitaliers qui ont déclaré au moins un cas en France?
#il y a un mois
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-etablissements-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('nb')
pip7 = Pipeline(table)
pip7.ajout_etape(TransformationTemporelle('2021-04-12','2021-04-12'))
res7 = pip7.applique()
pip7.ajout_etape(TransformationSpatiale(2,0))
res7 = pip7.applique()
print('le nombre de services ayant déclaré au moins un casil y a un mois est :')
print(table.contenu[0][2])


#actuellement
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-etablissements-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('nb')
pip7 = Pipeline(table)
pip7.ajout_etape(TransformationTemporelle('2021-05-12','2021-05-12'))
res7 = pip7.applique()
pip7.ajout_etape(TransformationSpatiale(2,0))
res7 = pip7.applique()
print('le nombre de services ayant déclaré au moins un cas actuellement est :')
print(table.contenu[0][2])

