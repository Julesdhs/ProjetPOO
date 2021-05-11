from EstimateurAbstraite import EstimateurAbstraite
from Table import Table

class EstimateurSomme(EstimateurAbstraite):
    def __init__(self,nom_col):
        self.nom_col=nom_col
    
    @staticmethod
    def somme(table,nom_col):
        indice = table.colonnes.index(nom_col)
        nb_obs = len(table.contenu)
        som = 0
        for ligne in range(nb_obs):
            som+= int(table.contenu[ligne][indice])
        return (som)

    def fit(self, table):
        res=Table(["somme de " + self.nom_col],  [EstimateurSomme.somme(table, self.nom_col)])
        return(res)
