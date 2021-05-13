from Importcsv import Import
from EstimateurSomme import EstimateurSomme
from Pipeline import Pipeline
import os

folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"


## Question 1): Quel est le nombre total d'hospitalisation dues au covid-19?
#on crée la table
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
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('incid_hosp')
#on crée la pipeline
Question2=Pipeline(table)
Question2.ajout_etape(TransformationTemporelle('jour','2021-05-05','2021-05-12'))
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
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
# Semaine1
debut_semaine1='2021-04-28'
fin_semaine1='2021-05-04'



pip2=Pipeline(table)
pip2.ajout_etape(TransformationTemporelle('jour',debut_semaine1,fin_semaine1))
pip2.ajout_etape(EstimateurMoyenne('incid_hosp'))
res2=pip2.applique()
print("le résultat pour la semaine dernière :")
print(res2[1].contenu)
#on trouve 14,11


# Semaine2
debut_semaine2='2021-05-05'
fin_semaine2='2021-05-12'
table=Import.creecsv(folder,filename)

Table3=Pipeline(table)
Table3.ajout_etape(TransformationTemporelle('jour',debut_semaine2,fin_semaine2))
Table3.ajout_etape(EstimateurMoyenne('incid_hosp'))
res3=Table3.applique()
print("le résultat pour cette semaine :")
print(res3[1].contenu)
#on trouve 10,46

##Question 4)Quel est le résultat de k-means avec k = 3 sur les données des départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours?
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
pip4 = Pipeline(table)
pip4.ajout_etape(TransformationTemporelle('jour','2021-01-01','2021-01-31'))
pip4.ajout_etape(MoyenneGlissante(7,'incid_hosp'))
pip4.ajout_etape(MoyenneGlissante(7,'incid_rea'))
pip4.ajout_etape(MoyenneGlissante(7,'incid_dc'))
pip4.ajout_etape(MoyenneGlissante(7,'incid_rad'))
pip4.ajout_etape(TransformationSelectionVariables(['dep','jour','moyenne_gincid_hosp', 'moyenne_gincid_rea', 'moyenne_gincid_dc', 'moyenne_gincid_rad']))
pip4.ajout_etape(EstimateurKmeans(3,['moyenne_gincid_hosp', 'moyenne_gincid_rea', 'moyenne_gincid_dc', 'moyenne_gincid_rad']))
res4 = pip4.applique()

#on exporte le tableau dans le dossier où sont les données
os.chdir(folder)
table.export('K-means.csv')


##Question 5)Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?
filename = "VacancesScolaires.json"
table5=Import.creejson(folder,filename) # Cela nous retourne une liste de deux tables, la table du calendrier et celle des académies
# On récupère seulement celle des académies
table5_calendar=table5[0]
table5_calendar.contenu=table5_calendar.contenu[1:]
pip5=Pipeline(table5_calendar)
# On commence par faire un fenetrage sur le l'année 2020
pip5.ajout_etape(TransformationTemporelle('Debut','2020-01-01','2020-12-31'))
pip5.applique()
# Etape 2 : On récupère les dates des vacances dce la Toussaint
indvac=table5_calendar.colonnes.index('Description')
ind_debut=table5_calendar.colonnes.index('Debut')
ind_fin=table5_calendar.colonnes.index('Fin')
for ligne in table5_calendar.contenu:
    if ligne[indvac] == 'Vacances de la Toussaint':
        date_debut=ligne[ind_debut]
        date_fin=ligne[ind_fin]
        break
# On selectionne la semaine suivant les vacances de la Toussaint
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('incid_rea')
pip6=Pipeline(table)
pip6.ajout_etape(TransformationTemporelle('jour',date_fin,delta=7))
pip6.applique()
pip6.ajout_etape(EstimateurSomme('incid_rea'))
res6=pip6.applique()
print(res6[0].contenu)

## Question 6) Quel est le nombre de décès(à l'hopital) totaux à ce jour par région et selon les sexes?
#on crée la table
filename = "donnees-hospitalieres-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('dc')
pip6 = Pipeline(table)
pip6.ajout_etape(TransformationSelectionVariables(['dep','sexe','jour','dc']))
res6 = pip6.applique()
pip6.ajout_etape(TransformationTemporelle('jour','2021-05-12','2021-05-12'))
res6 = pip6.applique()
pip6.ajout_etape(TransformationSpatiale(1,0))
res6 = pip6.applique()

#on exporte le tableau dans le dossier où sont les données
os.chdir(folder)
table.export('question6.csv')

## Question 7) Quel est le nombre de services hospitaliers qui ont déclaré au moins un cas en France?
#il y a un mois
filename = "donnees-hospitalieres-etablissements-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('nb')
pip7 = Pipeline(table)
pip7.ajout_etape(TransformationTemporelle('jour','2021-04-12','2021-04-12'))
res7 = pip7.applique()
pip7.ajout_etape(TransformationSpatiale(2,0))
res7 = pip7.applique()
print('le nombre de services ayant déclaré au moins un cas il y a un mois est :')
print(table.contenu[0][2])


#actuellement
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-etablissements-covid19-2021-05-12-19h05.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('nb')
pip7 = Pipeline(table)
pip7.ajout_etape(TransformationTemporelle('jour','2021-05-12','2021-05-12'))
res7 = pip7.applique()
pip7.ajout_etape(TransformationSpatiale(2,0))
res7 = pip7.applique()
print('le nombre de services ayant déclaré au moins un cas actuellement est :')
print(table.contenu[0][2])


## Question 8): Quel est le nombre cumulé de personnes décédées de 0 à 9 ans en comparaison aux personnes de plus de 90 ans?
filename = "donnees-hospitalieres-classe-age-covid19-2021-05-12-19h05 (1).csv"
table=Import.creecsv(folder,filename)
pip8 = Pipeline(table)
pip8.ajout_etape(TransformationTemporelle('jour','2021-05-12','2021-05-12'))
pip8.ajout_etape(TransformationSelectionVariables(['reg','cl_age90','dc']))
res8 = pip8.applique()
nb = [0,0]
for ligne in table.contenu:
    if ligne[0]== '53':
        if ligne[1] == '9':
            nb[0]=ligne[2]
        elif ligne[1] == '90':
            nb[1]= ligne[2]
print('le nombre de décès de moins de 9 ans et de plus de 90 ans en Bretagne est :')
print(nb)


