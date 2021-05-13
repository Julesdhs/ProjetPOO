from TransformationSelectionVariables import TransformationSelectionVariables

class TransformationSelectionVariables(TransformationAbstraite):
    '''la classe permet de ne garder que certaines variables/colonnes 
    de la table d'entrée en choississant le nom des variables à garder

    Attribus
    ----------
    variable : list[str] 
        liste des noms des variables à garder dans notre table
    valeur par défaut : []
    '''
    
    
    def __init__(self,variables = []):
    """ Constructeur de la classe TransformationSelectionVariables

    Paramètres
    ----------
    variables : list[str]
        liste des noms des variables à garder dans notre table
    valeur par défaut : []
    """        
        self.variables = variables
        
        
    def transform(self,table):
    """ Méthode transform de la classe TransformationSelectionVariables 

        Cette méthode permet d'effectuer la séléction de vaiables.
        Pour cela, on crée la liste d'indices associées à la liste des variables, 
        puis on enlève les colonnes des variables dont les indices ne sont pas dans la liste.

        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la sélection de variables

        Retours
        -------
        Ne retourne rien. Modifie in place la table.

    """
        listind = []
        for x in self.variables :
            listind.append(table.colonnes.index(x))
        n = len(table.contenu[0])
        for c in reversed(range(n)):
            if c not in listind :
                table.enlevcol(c + 1)








