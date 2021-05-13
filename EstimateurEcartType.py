from EstimateurAbstraite import EstimateurAbstraite
from EstimateurVariance import EstimateurVariance

class EstimateurEcartType (EstimateurAbstraite,EstimateurVariance):
    def __init__(self,nom_col):
        self.nom_col=nom_col
    
    @staticmethod
    def ecarttype(table,nom_col):
        return((EstimateurVariance.variance(table,nom_col))**0.5)

    def fit(self,table):
        table_resultat=Table(["écart-type de" + self.nom_col], [ecarttype(table,self.nom_col)])
        return(table_resultat)