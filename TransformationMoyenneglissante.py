from TransformationAbstraite import TransformationAbstraite

class TransformationMoyenneglissante(TransformationAbstraite):
    def __init__(self,periode):
        self.periode=periode
    
    def transform(self,table,nomcol):
        table_moy_glissante=Table("Moyenne glissante")
        longueurtable=len(table)
        for ligne in range (longueurtable-self.periode):
            EstimateurMoyenne.moyenne(table[ligne:ligne+self.periode-1],nomcol)
            ajoutlig(self,moyenne_p)
        return(table_moy_glissante)
        