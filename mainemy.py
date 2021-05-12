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


## Question 1): Quel est le nombre total d'hospitalisation dues au covid-19?
#on crée la table
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('incid_hosp')
table.stringtoint('incid_rea')
table.stringtoint('incid_dc')
table.stringtoint('incid_rad')
#on crée la pipeline
Question1=Pipeline(table)
Question1.ajout_etape(EstimateurSomme('incid_hosp'))
res1=Question1.applique()
#on retourne le résultat
print(res[0].contenu)

## Question 2) Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département?
#on crée la table
folder = "C:/Users/leonk/Documents/ProjetPOO-master/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)
table.stringtoint('incid_hosp')
table.stringtoint('incid_rea')
table.stringtoint('incid_dc')
table.stringtoint('incid_rad')
#on crée la pipeline
today = '2021-03-03'
Question2=Pipeline(table)
Question2.ajout_etape(TransformationTemporelle('2021-02-25','2021-03-03'))
Question2.applique()
#on fait des modifications
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
        


##Question 3) Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à celle de la semaine dernière?

