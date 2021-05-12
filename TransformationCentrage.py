#from TransformationAsbtraite import TransformationAbstraite

class TransformationCentrage(TransformationAbstraite):

    def transform(self,table):
        for i in range(len(table.colonnes)):
            moy = EstimateurMoyenne.moyenne(table,table.colonnes[i])
            for j in range(len(table.contenu)) :
                table.contenu[j][i] = table.contenu[j][i] - moy

#testé 05/05 14h


