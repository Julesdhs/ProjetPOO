import random
from EstimateurAbstraite import EstimateurAbstraite

class EstimateurKmeans(EstimateurAbstraite):
    '''Le processus utilisé ici est : on ajoute une colonne qui sert à noter la classe de chaque observation, puis on fait les calculs sur les variables isolées dans listcol, la table d'origine est alors modifiée avec une colonne en plus qui correspond à la classe de chaque observation'''

    def __init__(self,k,listcol):
        self.k = k
        self.listcol = listcol

    def calcul_centres(table,centres,k,nbvar,indclasse):
        '''calcule le barycentre des classes'''
        for i in range(k):
            nbelem = 0
            cent=[0 for m in range(nbvar)]
            for c in range(len(table.contenu)):
                if table.contenu[c][indclasse] == i :
                    nbelem += 1
                    for p in range(nbvar):
                        cent[p]+=table.contenu[c][p]
            for p in range(nbvar):
                if nbelem != 0 :
                    cent[p]=cent[p]/nbelem
                if nbelem == 0:
                    cent = [int(random.random()*10) for j in range(nbvar)]
            centres[i]=cent

    def distance(a,b,nbvar):
        '''calcule et renvoie la distance euclidienne entre deux vecteurs'''
        d=0
        for i in range(nbvar):
            d+=(a[i]-b[i])**2
        return(d**(1/2))

    def extrait_colonne(table,nomcol):
        '''renvoie un doublet nom,colonne d'une colonne d'un tableau à partir de son nom (semblable à celle utilisée dans jointure) '''
        indice=table.colonnes.index(nomcol)
        colonne_extraite=[]
        for ligne in table.contenu:
            colonne_extraite.append(ligne[indice])
        return (nomcol,colonne_extraite)

    def arrange_ordre(table,listcol):
        '''change l'ordre des colonnes en mettant les colonnes de la liste au début, et ajoute une colonne de zéros pour noter les classes, on garde les autres colonnes pour garder la vision générale lors de l'algo, arbitrairement'''
        T=Table(['Classes'],[[0] for k in range(len(table.contenu))])
        for nomcol in listcol :
            t=EstimateurKmeans.extrait_colonne(table,nomcol)
            Table.ajoutcol(T,t[0],t[1],1)
            '''syntaxe bizarre mais la normale avec T.ajoutcol ne fonctionnait pas jcp pourquoi'''
        for nomcol in table.colonnes :
            if nomcol not in listcol :
                t=EstimateurKmeans.extrait_colonne(table,nomcol)
                Table.ajoutcol(T,t[0],t[1])
        return(T,len(listcol))

    def fit(self,table0):
        table,nbvar=EstimateurKmeans.arrange_ordre(table0,self.listcol)
        k=self.k
        for nomcol in self.listcol :
            table.stringtoint(nomcol)
        N=TransformationNormalisation(self.listcol)
        N.transform(table)
        nb_obs=len(table.contenu)
        indclasse=table.colonnes.index('Classes')
        centres=[[int(random.random()*10) for j in range(nbvar)] for i in range(k)]
        classes=EstimateurKmeans.extrait_colonne(table,'Classes')[1]
        classes2=[[-1] for k in range(len(table.contenu))]

        nb=0
        while classes != classes2 and nb<50:
            '''nb est un cap arbitraire pas trop grand pour éviter les boucles infinies si une observation oscille'''
            nb+=1
            classes2=[[classes[k]] for k in range(len(table.contenu))]
            for j in range (nb_obs):
                d = 9999
                indice = 0
                for i in range (k):
                    dc=EstimateurKmeans.distance(table.contenu[j],centres[i],nbvar)
                    if d >= dc :
                        indice=i
                        d=dc
                table.contenu[j][indclasse] = indice
            EstimateurKmeans.calcul_centres(table,centres,k,nbvar,indclasse)
            classes=EstimateurKmeans.extrait_colonne(table,'Classes')[1]
        table0.ajoutcol('Classes',classes)

#testé 12/05 12h
