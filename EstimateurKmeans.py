import random

class EstimateurKmeans(EstimateurAbstraite):
    def __init__(self,k):
        self.k = k

    def calcul_centres(classes,centres,k,nbvar):
            for i in range(k):
                cent=[0 for m in range(nbvar)]
                nbelem=len(classes[i])
                for p in range(nbvar):
                    for j in range(nbelem):
                        cent[p]+=classes[i][j][p]
                for p in range(nbvar):
                    cent[p]=cent[p]/nbelem
                centres[i]=cent

    def distance(a,b):
        nbv=len(a)
        d=0
        for i in range(nbv):
            d+=(a[i]-b[i])**2
        return(d**(1/2))

    def Kmeans(self,table):
        k=self.k
        TransformationNormalisation.transform(table)
        nbvar=len(table.colonnes)
        nb_obs=len(table.contenu)
        centres=[[int(random.random()*10) for j in range(nbvar)] for i in range(k)]
        classes=[[] for i in range (k)]
        classes2=[[] for i in range (k)]
        nb=0
        for i in range(k):
            classes[i].append(centres[i])
        while classes != classes2 and nb<200:
            nb+=1
            classes2=classes
            for j in range (nb_obs):
                d=9999
                for i in range (k):
                    dc=EstimateurKmeans.distance(table.contenu[j],centres[i])
                    if d >= dc :
                        indice=i
                        d=dc
                classes[indice].append(table.contenu[j])
        EstimateurKmeans.calcul_centres(classes,centres,k,nbvar)
        return(centres,classes)

#testé 05/05 14h
