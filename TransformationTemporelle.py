#from TransformationAbstraite import TransformationAbstraite

class TransformationTemporelle(TransformationAbstraite):
    def __init__(self,debut_periode,fin_periode):
        self.debut_periode = debut_periode
        self.fin_periode = fin_periode

    def transform(self,table):

        '''les données sont classées par ordre temporel et la date est un jour, noté par la variable jour dans les tables, on considère des inégalités larges dans debut_periode et strictes pour fin_periode
        Si les données ne sont pas classées par odre temporel il faudra utiliser le module date time et trier les données au préalable : ce n'est pas notre cas ici'''

        if 'jour' in table.colonnes:
            newtable=Table()
            ind = table.colonnes.index('jour')
            for ligne in table.contenu:
                if ligne[ind]>= self.debut_periode and ligne[ind]<= self.fin_periode:
                    newtable.ajoutlig(ligne)
            table.contenu=newtable.contenu
            table.enlevlig(1)
        else:
            newtable=Table()
            ind = table.colonnes.index('Debut')
            for ligne in table.contenu:
                if ligne[ind]>= self.debut_periode and ligne[ind]<= self.fin_periode:
                    newtable.ajoutlig(ligne)
            table.contenu=newtable.contenu
            table.enlevlig(1)   


















