import os
folder = "C:/Users/jules/Desktop/POO/PPOO/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"

os.chdir(folder)

t=Import.creecsv(folder,filename)
#table=T.transform(t)
#table.export('blabla.csv')
#t2=Import.creecsv(folder,'blabla.csv')
#t2.colonnes = ['dep','jour','hosp', 'rea', 'rad', 'dc']
T2=TransformationSommeVar('jour','dep',['incid_hosp', 'incid_rea', 'incid_dc', 'incid_rad'])
table2=T2.transform(t)



