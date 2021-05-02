from EstimateurAbstraite import EstimateurAbstraite

class EstimateurVariance(EstimateurAbstraite):
   
    @staticmethod
    def variance (table,nom_col):
        indice=table.colonnes.index(nom_col)
        nb_obs=len(table.contenu)
        moy=table.moyenne()
        var=0
        for ligne in range nb_obs:
            var+=table.contenu[ligne][indice]**2
        return(var/nb_obs-moy**2) 

    
    def fit(table):
        table_resultat=Table()
        table_resultat.ajoutcol("variance de" + nom_col, [table.moyenne()])
        return(table_resultat)