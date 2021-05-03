from TransformationAsbtraite import TransformationAbstraite

class TransformationCentrage(TransformationAbstraite):
    def transform(table):
        for i in range(len(table.colonnes)):
            moy = moyenne(table,table.colonnes(i))
            for j in table.contenu :
                j[i]= j[i] - moy




