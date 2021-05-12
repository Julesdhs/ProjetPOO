#from TransformationAsbtraite import TransformationAbstraite

class TransformationCentrage(TransformationAbstraite):
    def __init__(self,listcol):
        self.listcol = listcol

    def transform(self,table):
        for nomcol in self.listcol:
            i=table.colonnes.index(nomcol)
            moy = EstimateurMoyenne.moyenne(table,table.colonnes[i])
            for j in range(len(table.contenu)) :
                table.contenu[j][i] = table.contenu[j][i] - moy

#testé 05/05 14h


