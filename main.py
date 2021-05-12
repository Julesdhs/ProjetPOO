import os

folder = "C:/Users/jules/Desktop/POO/PPOO/Donnees/Données/"
filename = "covid-hospit-incid-reg-2021-03-03-17h20.csv"

os.chdir(folder)

t=Import.creecsv(folder,filename)
txt=Import.creejson(folder,"VacancesScolaires.json")
print(txt[0].contenu[200])
t.export('test3.csv')

P1=Pipeline(t)
P1.ajout_etape(EstimateurMoyenne('incid_rea'))
P1.applique()

def g():
    '''
m=EstimateurMoyenne('incid_rea')
print(m.process(t).contenu[0])

tb=Table()
tt=Table(['test','test','test','test','test'],[['a','a1','a2','a3','a4'],['b','a','a','a','a'],['c','a','a','a','a']])
tt.ajoutcol('ajout',[1,2,3],2)
tt.enlevcol(4)
tt.ajoutlig(['a','a1','a2','a3','a4'])
tt.enlevlig(1)

kme=Table(['test1','test2','test3','test4','test5'],[[6,7,8,9,10],[-20,2,3,4,40],[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[21,22,23,24,25],[6,7,8,9,10],[21,22,23,24,25],[21,22,23,24,25],[21,22,23,24,25],[21,22,23,24,25],[21,200,23,24,25],[21,22,23,24,25]])


tj=Table(['t1','t2','t1','t3','t1','t5'],[[1,4,1,7,1,1],[2,5,2,8,2,2],[3,6,3,9,3,3]])
tj2=Table(['t1','t22','t5','t33','t5','t5','t1'],[[1,10,1,13,7,1,1],[20,11,20,14,8,20,20],[3,12,3,15,9,3,3]])

#res=EstimateurKmeans.Kmeans(kme,3)
#print(res[0][1],res[1][1])
#TransformationNormalisation.transform(kme)
jointu=TransformationJointure(tj2,'t1')
tjj=TransformationJointure.transform(jointu,tj)

TransformationJointure.delcol('t1',tj,tj2)
'''

#from Importcsv import Import
#from TransformationMoyenneglissante import TransformationMoyenneglissante

folder = "C:/Users/jules/Desktop/POO/PPOO/Donnees/Données/"
filename = "donnees-hospitalieres-covid19-2021-03-03-17h03.csv"
t=Import.creecsv(folder,filename)
t.stringtoint('hosp')
t.stringtoint('rea')
t.stringtoint('rad')
t.stringtoint('dc')


#a = TransformationMoyenneglissante(7,['hosp'])
#a.transform(t)

folder = "C:/Users/jules/Desktop/POO/PPOO/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)

Question1=Pipeline(table)
Question1.ajout_etape(EstimateurSomme('incid_hosp'))
print(Question1.applique()[0].contenu)

folder = "C:/Users/jules/Desktop/POO/PPOO/Donnees/Données/"
filename = "donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv"
table=Import.creecsv(folder,filename)

debut_semaine1='09\10\2020'
fin_semaine1='16\10\2020'
debut_semaine2='16\10\2020'
fin_semaine2='25\10\2020'

# Semaine1
Table2=Pipeline(table)
Table2.ajout_etape(TransformationTemporelle(debut_semaine1,fin_semaine1))
Table2.ajout_etape(EstimateurMoyenne('incid_hosp'))
print(Table2.applique()[1].contenu)

# Semaine2
Table3=Pipeline(table)
Table3.ajout_etape(TransformationTemporelle(debut_semaine2,fin_semaine2))
Table3.ajout_etape(EstimateurMoyenne('incid_hosp'))
print(Table3.applique()[1].contenu)
