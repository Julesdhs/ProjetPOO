from EstimateurAbstraite import EstimateurAbstraite
from Table import Table

class EstimateurMoyenne():
    '''la classe permet de calculer la moyenne sur une variable que l'on sélectionne à l'aide de nom_col dans une tale
    
    Attribus
    ----------
    nom_col : str
        nom de la variable dans notre table sur laquelle on veut effectuer notre moyenne
    '''
    
    def __init__(self,nom_col):
        """ Constructeur de la classe EstimateurMoyenne
        
        Paramètres
        ----------
        nom_col : str
        nom de la variable dans notre table sur laquelle on veut effectuer notre moyenne
        """       
        self.nom_col = nom_col

    @staticmethod
    def moyenne(table,nom_col):
        """ Méthode statique moyenne de la classe EstimateurMoyenne
    
        Cette méthode permet d'effectuer la moyenne d'une variable d'une table.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la moyenne
        nom_col : str
            nom de la variable dans notre table sur laquelle on veut effectuer notre moyenne
        
        Retours
        -------
        res : Table
            table contenant la moyenne demandée
        """
        indice = table.colonnes.index(nom_col)
        nb_obs = len(table.contenu)
        moy = 0
        for ligne in range(nb_obs):
            moy += int(table.contenu[ligne][indice])
        return (moy / nb_obs)

    def fit(self, table):
        """ Méthode statique fit de la classe EstimateurMoyenne
    
        Cette méthode permet d'effectuer la moyenne d'une variable d'une table.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la moyenne
        nom_col : str
            nom de la variable dans notre table sur laquelle on veut effectuer notre moyenne
        
        Retours
        -------
        res : Table
            table contenant la moyenne demandée
        """
        return Table(["moyenne de" + self.nom_col], [EstimateurMoyenne.moyenne(table, self.nom_col)])
