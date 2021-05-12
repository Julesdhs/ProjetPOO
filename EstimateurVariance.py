from EstimateurAbstraite import EstimateurAbstraite

class EstimateurVariance(EstimateurAbstraite):
    def __init__(self,nom_col):
        self.nom_col=nom_col
    
    @staticmethod
    def variance (table,nom_col):
        indice=table.colonnes.index(nom_col)
        nb_obs=len(table.contenu)
        moy=table.moyenne()
        var=0
        for ligne in range nb_obs:
            var+=table.contenu[ligne][indice]**2
        return(var/nb_obs-moy**2) 

    
    def fit(self,table):
        table_resultat=Table(["variance de" + nom_col], [variance(table,self.nomcol)])
        return(table_resultat)
