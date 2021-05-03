from TransformationAsbtraite import TransformationAbstraite

class TransformationTemporelle(TransformationAsbtraite):
    def __init__(self,debut_periode,fin_periode):
        self.debut_periode = debut_periode
        self.fin_periode = fin_periode


    def transform(self,table):

        '''les données sont classées par ordre temporel et la date est un jour, noté par la variable jour dans les tables, on considère des inégalités larges dans debut_periode et fin_periode. '''

        ind = table.colonnes.index(jour)
        n=len(table.contenu)
        for l in range(n) :
            x = table.contenu[l][ind]
            while x != self.debut_periode :
                table.enlevlig(l)
            if x == self.fin_periode:
                indfin = l

        for i in range(indfin + 1,l):
            table.enlevelig(i)












