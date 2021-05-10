import os


folder = "P:/PPOO/Donnees/Données/"
filename = "covid-hospit-incid-reg-2021-03-03-17h20.csv"

os.chdir(folder)

t=Import.cree(folder,filename)
'''
t.export('test3.csv')
P1=Pipeline(t)
P1.ajout_etape(EstimateurMoyenne('incid_rea'))
P1.applique()
'''
m=EstimateurMoyenne('incid_rea')
print(m.process(t).contenu[0])

tb=Table()
tt=Table(['test','test','test','test','test'],[['a','a1','a2','a3','a4'],['b','a','a','a','a'],['c','a','a','a','a']])
tt.ajoutcol('ajout',[1,2,3],2)
'''tt.enlevcol()'''
tt.ajoutlig(['a','a1','a2','a3','a4'])
tt.enlevlig(1)
'''
kme=Table(['test1','test2','test3','test4','test5'],[[6,7,8,9,10],[-20,2,3,4,40],[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[21,22,23,24,25],[6,7,8,9,10],[21,22,23,24,25],[21,22,23,24,25],[21,22,23,24,25],[21,22,23,24,25],[21,200,23,24,25],[21,22,23,24,25]])
tj=Table(['t1','t2','t3'],[[1,4,7],[2,5,8],[3,6,9]])
tj2=Table(['t1','t22','t33','t3'],[[1,10,13,7],[20,11,14,8],[3,12,15,9]])
#res=EstimateurKmeans.Kmeans(kme,3)
#print(res[0][1],res[1][1])
#TransformationNormalisation.transform(kme)
jointu=TransformationJointure(tj2,'t1')
tjj=TransformationJointure.transform(jointu,tj)
'''
