#from Table import Table

class TransformationJointure(TransformationAbstraite):
    def __init__(self,table,nomcol):
        self.table = table
        self.nomcol = nomcol

    def extrait_colonne(table,nomcol):
        indice=table.colonnes.index(nomcol)
        colonne_extraite=[]
        for ligne in table.contenu:
            colonne_extraite.append([ligne[indice]])
        return Table([nomcol],colonne_extraite)

    def extrait_table(nomcol,table):
        return([TransformationJointure.extrait_colonne(table,nomcol)]+[TransformationJointure.extrait_colonne(table,table.colonnes[k]) for k in range(len(table.colonnes)) if (table.colonnes[k] != nomcol)])

    def delcol(clef,table1,table2):
        for nomcol in table1.colonnes :
            if nomcol != clef :
                if nomcol in table2.colonnes:
                    Table.enlevcol(table2,table2.colonnes.index(nomcol))


    def prepare(self,table1,table2):
        t1=TransformationJointure.extrait_table(self.nomcol,table1)
        t2=TransformationJointure.extrait_table(self.nomcol,table2)
        for col in t1 :
            if col in t2 :
                del t2[t2.contenu.index(col)]
        return t1,t2

    def transform(self,table2,gauche=True):
        TransformationJointure.delcol(self.nomcol,table2,self.table)
        (t2,t1)=TransformationJointure.prepare(self,self.table,table2)
        tj=Table([t1[0].colonnes[0]],[[t1[0].contenu[k][0]] for k in range(len(t1[0].contenu))])
        for val in t1[0].contenu :
            if val in t2[0].contenu :
                '''si la valeur est dans la 2e table on ajoute tout le reste'''
                indiceval=t1[0].contenu.index(val)
                indicevalt2=t2[0].contenu.index(val)

                for k in range(len(t1)-1):
                    tj.contenu[indiceval].append(t1[k+1].contenu[indiceval][0])


                for k in range(len(t2)-1):
                    tj.contenu[indiceval].append(t2[k+1].contenu[indicevalt2][0])

            if gauche :
                if val not in t2[0].contenu :
                    indiceval=t1[0].contenu.index(val)
                    '''sinon, et si on fait une jointure à gauche, on met des 0'''
                    for k in range(len(t1)-1):
                        tj.contenu[indiceval].append(t1[k+1].contenu[indiceval][0])


                    for k in range(len(t2)-1):
                        tj.contenu[indiceval].append(0)

        return tj






