from EstimateurAbstraite import EstimateurAbstraite
from EstimateurVariance import EstimateurVariance

class EstimateurEcartType (EstimateurAbstraite):
    '''la classe permet de calculer l'écart-type sur une variable que l'on sélectionne à l'aide de nom_col
    
    Attribus
    ----------
    nom_col : str
        nom de la variable dans notre table sur laquelle on veut effectuer notre écart-type
        
    '''
    
    def __init__(self,nom_col):
        """ Constructeur de la classe EstimateurEcartType
    Paramètres
    ----------
    nom_col : str
        nom de la variable dans notre table sur laquelle on veut effectuer notre écart-type
        """       
        self.nom_col=nom_col
    
    @staticmethod
    def ecarttype(table,nom_col):
        """ Méthode statique ecarttype de la classe EstimateurEcartType
    
        Cette méthode permet d'effectuer l'écart-type d'une variable d'une table.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la écart-type
        nom_col : str
            nom de la variable dans notre table sur laquelle on veut effectuer notre écart-type
        """
        return((EstimateurVariance.variance(table,nom_col))**0.5)

    def fit(self,table):
         """ Méthode fit de la classe EstimateurEcartType
    
        Cette méthode permet d'effectuer l'écart-type d'une variable d'une table.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la écart-type
        nom_col : str
            nom de la variable dans notre table sur laquelle on veut effectuer notre écart-type
        
        Retours
        -------
        res : Table
            table contenant l'écart-type demandé
        """
        table_resultat=Table(["écart-type de" + self.nom_col], [ecarttype(table,self.nom_col)])
        return(table_resultat)
