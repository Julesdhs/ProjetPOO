folder = "C:/Users/leonk/Documents/projet/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"
t=Import.cree(folder,filename)
t.stringtoint('hosp')
t.stringtoint('rea')
t.stringtoint('rad')
t.stringtoint('dc')
spat = TransformationSpatiale(1,0)
spat.transform(t)

import os
os.chdir(folder)

t.export('a.csv')

selec = TransformationSelectionVariables([])








