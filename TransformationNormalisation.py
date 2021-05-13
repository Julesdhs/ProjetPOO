from TransformationAsbtraite import TransformationAbstraite
from TransformationCentrage import TransformationCentrage
from EstimateurVariance import EstimateurVariance

class TransformationNormalisation(TransformationAbstraite):
    '''la classe permet de normaliser un certain nombre de colonnes d'une table.
    
    Attribus
    ----------
    liste_colonnes : list[str]
        liste des nom de colonnes de la table à normaliser
    '''
    def __init__(self, liste_colonnes):
        """ Constructeur de la classe TransformationNormalisation
        
        Paramètres
        ----------
        liste_colonnes : list[str]
            liste des nom de colonnes de la table à normaliser
        """   
        self.liste_colonnes=liste_colonnes

    def transform(self,table):
        """ Méthode transform de la classe TransformationNormalisation 
    
        Cette méthode permet d'effectuer la la normalisation d'une liste de variables de la table.
        Elle utilise la méthode transform de la TranformationCentrage et la variance de l'EstimateurVariance.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la normalisation

        """
        c=TransformationCentrage(self.liste_colonnes)
        c.transform(table)
        for nomcol in self.liste_colonnes:
            i = table.colonnes.index(nomcol)
            var = EstimateurVariance.variance(table,table.colonnes[i])
            if var != 0:
                for l in table.contenu:
                    l[i]= round(l[i]/(var**(1/2)),2)






