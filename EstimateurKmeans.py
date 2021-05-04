from EstimateurAbstraite import EstimateurAbstraite
import random 
class EstimateurKmeans (EstimateurAbstraite):
    def Kmeans (table,k):
        p=len(table.colonnes)
        nb_obs=len(table.contenu)
        centres=[[[random.random()*100] for j in range(p)]] for i in range(k)]
        classes=[[] for i in range (k)]
        classes2=[[] for i in range (k)]
        while classes != classes2 :
            classes2=classes
            for j in range (nb_obs):
                d=9999 
                for i in range (k):
                    dc=distance(table.contenu[j],centres[i])
                    if d >= dc :
                        indice=i
                        d=dc
                classes[indice].append(table.contenu[j])        
        calcul_centres(classes,centres)
        
    def distance(a,b):
        nbv=len(a)
        d=0
        for i in range(nbv):
            d+=(a[i]-b[i])**2
        return(d**(1/2))
        
    def calcul_centres(classes,centres):
            for i_eme_classe in range (k):
                nb_ele_classe=len(classe[i_eme_classe])
                res=0
                for ele in classe[i_eme_classe]:
                    res+=ele
                res=res/nb_ele_classe
                centres[i_eme_classe]=res
            

