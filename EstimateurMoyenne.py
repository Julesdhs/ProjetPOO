#from EstimateurAbstraite import EstimateurAbstraite

class EstimateurMoyenne(EstimateurAbstraite):

    def __init__(self,nom_col):
        self.nom_col = nom_col

    @staticmethod
    def moyenne(table,nom_col):
        indice=table.colonnes.index(nom_col)
        nb_obs=len(table.contenu)
        moy=0
        for ligne in range(nb_obs):
            moy+=table.contenu[ligne][indice]
        return(moy/nb_obs)

    def fit(table):
        table_resultat=Table()
        table_resultat.ajoutcol("moyenne de" + nom_col, [table.moyenne(nom_col)])
        return(table_resultat)

#testé 05/05 14h
