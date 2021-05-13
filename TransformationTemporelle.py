from TransformationAbstraite import TransformationAbstraite
from datetime import datetime,timedelta

class TransformationTemporelle(TransformationAbstraite):
    '''La classe permet de ne conserver que certaines observations de la table 
    dont la date est comprise dans une période donnée.
    Pour selectionner la periode soit on a deux dates précises (de fin et de début), 
    soit une date et un temps delta définissant la durée de notre période.

    Attribus
    ----------
    nom_col : str
        nom de la colonne qui permet de faire le fenetrage
    
    debut_periode : str
        debut de la période qui permet de faire le fenetrage
    valeur par défaut : None
    
    fin_periode : str
        fin de la période qui permet de faire le fenetrage
    valeur par défaut : None
    
    delta : int
        durée de la période qui permet de faire le fenetrage
    valeur par défaut : None
    '''
    
    def __init__(self,nom_col,debut_periode=None,fin_periode=None,delta=None):
        """ Constructeur de la classe TransformationTemporelle
        Paramètres
        ----------
        nom_col : str
            nom de la colonne qui permet de faire le fenetrage

        debut_periode : str
            debut de la période qui permet de faire le fenetrage
        valeur par défaut : None

        fin_periode : str
            fin de la période qui permet de faire le fenetrage
        valeur par défaut : None

        delta : int
            durée de la période qui permet de faire le fenetrage
        valeur par défaut : None
        """   
        self.nom_col=nom_col
        if debut_periode != None:
            if delta != None:
                dp=datetime.strptime(debut_periode,'%Y-%m-%d')
                fp=dp+timedelta(delta)
                fin_periode=fp.strftime('%Y-%m-%d')
        if fin_periode != None:
            if delta != None:
                fp=datetime.strptime(fin_periode,'%Y-%m-%d')
                dp=fp-timedelta(delta)
                debut_periode=dp.strftime('%Y-%m-%d')     
        self.debut_periode = debut_periode
        self.fin_periode = fin_periode
   
    def transform(self,table):
        """ Méthode transform de la classe TransformationTemporelle
    
        Cette méthode permet d'effectuer le fenetrage de la table donnée en paramètre.

        
        Paramètres
        ----------
        table : Table
            table sur laquelle on veut effectuer le fenetrage
        
        """

        newtable=Table()
        ind = table.colonnes.index(self.nom_col)
        for ligne in table.contenu: # on parcourt toute la table et on cherche lorsque l'observation appartient à notre période
            if ligne[ind]>= self.debut_periode and ligne[ind]<= self.fin_periode:
                newtable.ajoutlig(ligne)
        table.contenu=newtable.contenu
#        table.enlevlig(1)





















