#from TransformationAbstraite import TransformationAbstraite

class TransformationTemporelle(TransformationAbstraite):
    def __init__(self,debut_periode,fin_periode):
        self.debut_periode = debut_periode
        self.fin_periode = fin_periode

    def transform(self,table):

        '''les données sont classées par ordre temporel et la date est un jour, noté par la variable jour dans les tables, on considère des inégalités larges dans debut_periode et strictes pour fin_periode
        Si les données ne sont pas classées par odre temporel il faudra utiliser le module date time et trier les données au préalable : ce n'est pas notre cas ici'''

        ind = table.colonnes.index('jour')
        n=len(table.contenu)
        newt = Table()
        l = 0
        x = table.contenu[l][ind]
        if x== self.debut_periode:
            while x!= self.fin_periode:
                newt.ajoutlig(table.contenu[l])
                l+=1
                x = table.contenu[l][ind]
        else:
            l+=1
            x = table.contenu[l][ind]
        table.contenu = newt.contenu















