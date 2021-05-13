from TransformationAsbtraite import TransformationAbstraite

class TransformationCentrage(TransformationAbstraite):
    '''la classe permet de centrer un certain nombre de colonnes d'une table.
    
    Attribus
    ----------
    listcol: list[str]
        liste des nom de colonnes de la table à centrer
    '''
    def __init__(self,listcol):
        """ Constructeur de la classe TransformationCentrage

        Paramètres
        ----------
        listcol: list[str]
            liste des nom de colonnes de la table à centrer
        """   
        self.listcol = listcol

    def transform(self,table):
        """ Méthode transform de la classe TransformationCentrage 
    
        Cette méthode permet d'effectuer la centralisation d'une liste de variables de la table.
        Elle utilise la méthode transform de la TranformationCentrage et la variance de l'EstimateurMoyenne.
        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer la centralisation
        """
        for nomcol in self.listcol:
            i=table.colonnes.index(nomcol)
            moy = EstimateurMoyenne.moyenne(table,table.colonnes[i])
            for j in range(len(table.contenu)) :
                table.contenu[j][i] = table.contenu[j][i] - moy



