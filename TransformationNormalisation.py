#from TransformationAsbtraite import TransformationAbstraite
#from TransformationCentrage import TransformationCentrage

# on définit le tableau centré réduit comme la classe fille de la classe pour les tableaux centrés

class TransformationNormalisation(TransformationCentrage):
    ''' on définit le tableau centré réduit comme la classe fille de la classe pour les tableaux centrés '''
    def __init__(self, liste_colonnes):
        self.liste_colonnes=liste_colonnes
        
    def transform(self,table):
        TransformationCentrage.transform(table)
        for i in range(len(table.colonnes)):
            var = EstimateurVariance.variance(table,table.colonnes[i])
            if var != 0:
                for l in table.contenu:
                    l[i]= round(l[i]/(var**(1/2)),2)


#testé 05/05 14h




