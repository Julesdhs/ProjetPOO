import csv as csv

# Dossier où se trouve le fichier :
folder = "C:/Users/jules/Desktop/POO/PPOO/Donnees/Données/"
filename = "covid-hospit-incid-reg-2021-03-03-17h20.csv"
data = []

with open(folder + filename, encoding ='ISO-8859-1') as csvfile :
    covidreader = csv.reader(csvfile, delimiter=';')
    for row in covidreader :
        data.append(row)

t='test'
def importtotable(list):
    return(Table(list[0], [list[k] for k in range(1,len(list))]) )

T=importtotable(data)

'''l=[1,2,3,4,5,6]
for pos in range(len(l)+1):
    print(l[:pos]+[10]+l[pos:],pos+1)'''

tb=Table()
tt=Table(['test','test','test','test','test'],[['a','a1','a2','a3','a4'],['b','a','a','a','a'],['c','a','a','a','a']])
tt.ajoutcol('ajout',[1,2,3],2)
tt.enlevcol()
tt.ajoutlig(['a','a1','a2','a3','a4'])
tt.enlevlig(1)
kme=Table(['test1','test2','test3','test4','test5'],[[6,7,8,9,10],[-20,2,3,4,40],[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[21,22,23,24,25],[6,7,8,9,10],[21,22,23,24,25],[21,22,23,24,25],[21,22,23,24,25],[21,22,23,24,25],[21,200,23,24,25],[21,22,23,24,25]])

#res=EstimateurKmeans.Kmeans(kme,3)
#print(res[0][1],res[1][1])
TransformationNormalisation.transform(kme)


