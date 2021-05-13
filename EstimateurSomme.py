from EstimateurAbstraite import EstimateurAbstraite

class EstimateurSomme(EstimateurAbstraite):
    '''la classe permet de calculer la somme sur une variable que l'on sélectionne à l'aide de nom_col
    
    Attribus
    ----------
    nom_col : str
        nom de la variable à garder dans notre table
    '''
    
    def __init__(self,nom_col):
    """ Constructeur de la classe EstimateurSomme
    Paramètres
    ----------
    nom_col : str
        nom de la variable dans notre table sur laquelle on veut effectuer notre somme
    """       
        self.nom_col=nom_col
    
    @staticmethod
    def somme(table,nom_col):
        """ Méthode statique fit de la classe EstimateurSomme
    
        Cette méthode permet d'effectuer la somme d'une variable d'une table.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la somme
        nom_col : str
            nom de la variable dans notre table sur laquelle on veut effectuer notre somme
        
        Retours
        -------
        res : Table
            table contenant la somme demandée
        """
        indice = table.colonnes.index(nom_col)
        nb_obs = len(table.contenu)
        som = 0
        for ligne in range(nb_obs):
            som+= int(table.contenu[ligne][indice])
        return (som)

    def fit(self, table):
    """ Méthode fit de la classe EstimateurSomme 
    
        Cette méthode permet d'effectuer la somme d'une variable.
        Pour cela, on appelle la méthode statique somme précédente.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la somme
        
        Retours
        -------
        res : Table
            table contenant la somme demandée
    """
    res=Table(["somme de " + self.nom_col],  [EstimateurSomme.somme(table, self.nom_col)])
        return(res)
