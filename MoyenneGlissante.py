class MoyenneGlissante(TransformationAbstraite):
    def __init__(self,periode,nomcol):
        self.periode = periode
        self.nomcolonnes = listecolonnes

    def transform(self,table):
        colonne = [[-1] for k in range(len(table.contenu))]
        p=self.periode
        table.stringtoint(nomcol)
        indcol = table.colonnes.index(col)
        for k in range(len(table.contenu)):
            if p + k < len(table.contenu):
                m = 0
                for i in range(p):
                    m += table.contenu[k+i][indcol]
                m = m/p
                colonne[k]=m
        table.ajoutcol('moyenne glissante de' + nomcol,colonne)