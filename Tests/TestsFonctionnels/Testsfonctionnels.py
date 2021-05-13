### Tests fonctionnels
from Importcsv import Import 
from OperationAbstraite import OperationAbstraite
from EstimateurSomme import EstimateurSomme
from TransformationTemporelle import TransformationTemporelle
from EstimateurMoyenne import EstimateurMoyenne
from Pipeline import Pipeline
from EstimateurAbstraite import EstimateurAbstraite

folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"
table=Import.cree(folder,filename)
table.stringtoint('hosp')
table.stringtoint('rea')
table.stringtoint('rad')
table.stringtoint('dc')

# Test de TransformationSelectionVariables
from TransformationSelectionVariables import TransformationSelectionVariables
folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"
table=Import.cree(folder,filename)
TransformationSelectionVariables(['jour','hosp']).transform(table)
print(table.colonnes,table.contenu[0])

# Test de TransformationSpatiale
from TransformationSpatiale import TransformationSpatiale
folder = "P:/PTD/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"
t=Import.cree(folder,filename)
t.stringtoint('hosp')
t.stringtoint('rea')
t.stringtoint('rad')
t.stringtoint('dc')
print(t.colonnes,t.contenu[0])
TransformationSpatiale(1,0).transform(t)
print(t.colonnes,t.contenu[0])

# Test de TransformationJointure
