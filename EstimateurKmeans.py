import random

class EstimateurKmeans(EstimateurAbstraite):

    def __init__(self,k,listevar):
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

    def extrait_colonne(table,nomcol):
        indice=table.colonnes.index(nomcol)
        colonne_extraite=[]
        for ligne in table.contenu:
            colonne_extraite.append([ligne[indice]])
        return nomcol,colonne_extraite

    def extrait_table(listcol,table):
        T=Table()
        for k in range(len(table.colonnes)):
            if table.colonnes[k] in listcol :
               T.ajoutcol(EstimateurKmeans.extrait_colonne(table,table.colonnes[k]))
        return(T)

    def Kmeans(self,T):
        table=extrait_table(self.listcol,T)
        k=self.k
        TransformationNormalisation.transform(table)
        table.ajoutcol('ordre')
        nbvar=len(table.colonnes)-1
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
        return(centres,classesr)

#testé 05/05 14h
