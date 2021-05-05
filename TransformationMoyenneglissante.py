from TransformationAbstraite import TransformationAbstraite

class TransformationMoyenneglissante(TransformationAbstraite):

    def __init__(self,periode,nom_col):
        self.periode=periode
        self.nom_col=nom_col

    def transform(self,table,nom_col):
        table_moy_glissante=Table("Moyenne glissante")
        longueurtable=len(table)
        for ligne in range (longueurtable-self.periode):
            EstimateurMoyenne.moyenne(table[ligne:ligne+self.periode-1],nom_col)
            ajoutlig(self,moyenne_p)
        return(table_moy_glissante)
