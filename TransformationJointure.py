from Table import Table

class TransformationJointure(TransformationAbstraite):
    def __init__(self,table,nomcol):
        self.table=table
        self.nomcol=nomcol

    def extrait_colonne(table,nomcol):
        indice=table.colonnes.index(nomcol)
        colonne_extraite=[]
        for ligne in table.contenu:
            colonne_extraite.append(ligne[indice])
        return(Table([nomcol],colonne_extraite))
        
    def extrait_table(nomcol,table):
        return([TransformationJointure.extrait_colonne(table,nomcol)]+[TransformationJointure.extrait_colonne(table,table.colonnes[k]) for k in range(len(table.colonnes)) if (table.colonnes[k] != nomcol)])
    
    def prepare(self,table1,table2):
        t1=TransformationJointure.extrait_table(self.nomcol,table1)
        t2=TransformationJointure.extrait_table(self.nomcol,table2)
        return(t1,t2)
        
    def transform(self,table2):
        (t1,t2)=prepare(self,self.table,table2)
        for val in t1[0].contenu :
            if val in t2[0].contenu : 
                indiceval=t1[0].contenu.index(val)
                for k in range(len(t1):
                    t1[0][indiceval]
                    
                
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





