from Table import Table

class TransformationJointure():
    def __init__(self,table1,table2,nomcol):
        self.table1=table1
        self.table2=table2
        self.nomcol=nomcol

    def extrait_colonne(table, nomcol):
        indice=table.colonnes.index(nomcol)
        colonne_extraite=[]
        for ligne in table.contenu:
            colonne_extraite.append(ligne[indice])
        return(Table([nomcol],colonne_extraite))
        
    def extrait_table(nomcol,table):
        return([TransformationJointure.extrait_colonne(table,nomcol)]+[TransformationJointure.extrait_colonne(table,table.colonnes[k]) for k in range(len(table.colonnes)) if (table.colonnes[k] != nomcol)])
    
    def prepare(self,table1,table2):
        clef1=table1.index(col2[ligne2])
        clef2=table2.index()
    def transform(self):
        nb_obs_table1=len(self.table1)
        nb_obs_table2=len(self.table2)

        table_jointure=Table(joint_nom_var(self), table1.contenu)
        col1=extrait_colonne(self.table1,self.nomcol)
        col2=extrait_colonne(self.table2,self.nomcol)
        for ligne2 in range(nb_obs_table2):
            if col2[ligne2] in col1:
                ligne1=col2.index(col2[ligne2])



    def joint_nom_var(self):
        colonnes=[]
        for nomcol1 in self.table1.colonnes:
            if nomcol1 not in colonnes:
                colonnes.append(nomcol1)
        for nomcol2 in self.table2.colonnes:
                if nomcol2 not in colonnes:
                    colonnes.append(nomcol2)

    def joint_contenu(self):
        pass





