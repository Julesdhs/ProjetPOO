#from TransformationAbstraite import TransformationAbstraite

from TransformationAbstraite import TransformationAbstraite
from Table import Table
from datetime import datetime,timedelta

class TransformationTemporelle(TransformationAbstraite):
    def __init__(self,nom_col,debut_periode=None,fin_periode=None,delta=None):
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

        '''les données sont classées par ordre temporel et la date est un jour, noté par la variable jour dans les tables, on considère des inégalités larges dans debut_periode et strictes pour fin_periode
        Si les données ne sont pas classées par odre temporel il faudra utiliser le module date time et trier les données au préalable : ce n'est pas notre cas ici'''
        newtable=Table()
        ind = table.colonnes.index(self.nom_col)
        for ligne in table.contenu:
            if ligne[ind]>= self.debut_periode and ligne[ind]<= self.fin_periode:
                newtable.ajoutlig(ligne)
        table.contenu=newtable.contenu
        table.enlevlig(1)





















