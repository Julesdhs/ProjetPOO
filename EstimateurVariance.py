#from EstimateurAbstraite import EstimateurAbstraite

class EstimateurVariance(EstimateurAbstraite):
     '''la classe permet de calculer la variance sur une variable que l'on sélectionne à l'aide de nom_col
     dans notre table
    
    Attribus
    ----------
    nom_col : str
        nom de la variable dans notre table sur laquelle on veut calculer notre variance
    '''
    
    def __init__(self,nom_col):
    """ Constructeur de la classe EstimateurVariance
    Paramètres
    ----------
    nom_col : str
        nom de la variable dans notre table sur laquelle on veut calculer notre variance
    """       
        self.nom_col=nom_col
    
    @staticmethod
    def variance (table,nom_col):
        """ Méthode statique variance de la classe EstimateurVariance
    
        Cette méthode permet d'effectuer la variance d'une variable d'une table.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la variance
        nom_col : str
            nom de la variable dans notre table sur laquelle on veut effectuer notre variance
        
        Retours
        -------
        res : Table
            table contenant la variance demandée
        """
        indice=table.colonnes.index(nom_col)
        nb_obs=len(table.contenu)
        moy=EstimateurMoyenne.moyenne(table,nom_col)
        var=0
        for ligne in range (nb_obs):
            var+=table.contenu[ligne][indice]**2
        return(var/nb_obs-moy**2) 

    
    def fit(self,table):
        """ Méthode fit de la classe EstimateurVariance
    
        Cette méthode permet d'effectuer la variance d'une variable.
        Pour cela, on appelle la méthode statique variance précédente.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la variance
        
        Retours
        -------
        res : Table
            table contenant la variance demandée
        """
        table_resultat=Table(["variance de" + nom_col], [variance(table,self.nomcol)])
        return(table_resultat)
