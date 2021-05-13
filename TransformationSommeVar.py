class TransformationSommeVar(TransformationAbstraite):
    def __init__(self,nomcol,varsupprimee,listsomme):
        self.nomcol = nomcol
        self.varsupprimee = varsupprimee
        self.listsomme = listsomme

    def transform(self,table):
        indicecol=table.colonnes.index(self.nomcol)
        for nomcol in self.listsomme :
            table.stringtoint(nomcol)
        #table=Table([T.colonnes[k] for k in range(len(T.colonnes))],[[T.contenu[k]]])
        T=Table()
        nbsupr = 0
        listgarde=[]
        k = 0
        i = 0
        while k+i<len(table.contenu)-2:
            if table.contenu[k][indicecol] == table.contenu[k+1+i][indicecol] :
                for varsomme in self.listsomme :
                    indicevar = table.colonnes.index(varsomme)
                    table.contenu[k][indicevar] += table.contenu[k+1+i][indicevar]
                i += 1

            if table.contenu[k][indicecol] != table.contenu[k+1+i][indicecol] :
                if i == 0 :
                    k = k + 1
                if i != 0 :
                    listgarde.append(k)
                    k = k + i
                    i = 0

        indicesupr = table.colonnes.index(self.varsupprimee)

        for k in range(len(table.colonnes)):
            T.colonnes.append(table.colonnes[k])

        #T.colonnes = T.colonnes[:indicesupr] + T.colonnes[indicesupr+1:]
        T.contenu.pop()
        for i in range(len(listgarde)):
            k = listgarde[i]
            T.contenu.append([table.contenu[k][j] for j in range(len(table.colonnes))])

        return(T)






