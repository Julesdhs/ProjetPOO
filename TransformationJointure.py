#from Table import Table

class TransformationJointure(TransformationAbstraite):

    def __init__(self,table,nomcol,gauche = True):
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
        for nomcol in table2.colonnes :
            if nomcol != clef :
                if nomcol in table2.colonnes:
                    Table.enlevcol(table2,table2.colonnes.index(nomcol)+1)


    def prepare(self,table1,table2):
        t1=TransformationJointure.extrait_table(self.nomcol,table1)
        t2=TransformationJointure.extrait_table(self.nomcol,table2)
        return t1,t2

    def transform(self,table2):
        TransformationJointure.delcol(self.nomcol,table2,self.table)
        (t2,t1)=TransformationJointure.prepare(self,self.table,table2)
        tj=Table([t1[0].colonnes[0]],[[t1[0].contenu[k][0]] for k in range(len(t1[0].contenu))])
        for k in range(len(t1)-1):
            tj.colonnes.append(t1[k+1].colonnes[0])
        for k in range(len(t2)-1):
            tj.colonnes.append(t2[k+1].colonnes[0])
        for val in t1[0].contenu :
            if val in t2[0].contenu :
                '''si la valeur est dans la 2e table on ajoute tout le reste'''
                indiceval=t1[0].contenu.index(val)
                indicevalt2=t2[0].contenu.index(val)

                for k in range(len(t1)-1):
                    tj.contenu[indiceval].append(t1[k+1].contenu[indiceval][0])


                for k in range(len(t2)-1):
                    tj.contenu[indiceval].append(t2[k+1].contenu[indicevalt2][0])

            if self.gauche :
                if val not in t2[0].contenu :
                    indiceval=t1[0].contenu.index(val)
                    '''sinon, et si on fait une jointure à gauche, on met des 0'''
                    for k in range(len(t1)-1):
                        tj.contenu[indiceval].append(t1[k+1].contenu[indiceval][0])


                    for k in range(len(t2)-1):
                        tj.contenu[indiceval].append(0)
        return tj


#from Table import Table

class TransformationJointure(TransformationAbstraite):

    def __init__(self,table,nomcol,gauche = True):
        self.table = table
        self.nomcol = nomcol
        self.gauche = gauche

    def extrait_colonne(table,nomcol):
        indice=table.colonnes.index(nomcol)
        colonne_extraite=[]
        for ligne in table.contenu:
            colonne_extraite.append([ligne[indice]])
        return Table([nomcol],colonne_extraite)

    def extrait_table(nomcol,table):
        L=[TransformationJointure.extrait_colonne(table,nomcol)]
        for cols in table.colonnes :
            if cols != nomcol :
                L.append(TransformationJointure.extrait_colonne(table,cols))
        return(L)
        
    def delcol(clef,table1,table2):
        for nomcol in table2.colonnes :
            if nomcol != clef :
                if nomcol in table2.colonnes:
                    Table.enlevcol(table2,table2.colonnes.index(nomcol)+1)


    def prepare(self,table1,table2):
        t1=TransformationJointure.extrait_table(self.nomcol,table1)
        t2=TransformationJointure.extrait_table(self.nomcol,table2)
        return t1,t2

    def transform(self,table2):
        TransformationJointure.delcol(self.nomcol,table2,self.table)
        (t2,t1)=TransformationJointure.prepare(self,self.table,table2)
        #print(t1[1].contenu,len(t1))
        print(t1[2].contenu,t2[1].contenu)
        tj=Table([t1[0].colonnes[0]],[[] for k in range(len(t2[0].contenu))])
        for k in range(len(t1)-1):
           #print(k)
            tj.colonnes.append(t1[k+1].colonnes[0])
        for k in range(len(t2)-1):
            tj.colonnes.append(t2[k+1].colonnes[0])
        for val in t2[0].contenu :
            if val in t1[0].contenu :
                '''si la valeur est dans la 2e table on ajoute tout le reste'''
                indiceval=t1[0].contenu.index(val)
                indicevalt2=t2[0].contenu.index(val)

                for k in range(len(t1)):
                    tj.contenu[indiceval].append(t1[k].contenu[indiceval][0])


                for k in range(len(t2)):
                    tj.contenu[indiceval].append(t2[k].contenu[indicevalt2][0])

        if self.gauche :
            '''si la valeur est dans la table de base et pas dans celle qu'on ajoute, on cherche où elle devrait être et on l'insère, cette méthode est peu efficace mais on l'utilise car on l'ajoute à un autre algo qui fait la jointure intersection '''
            for val in t1[0].contenu :
                if val not in t2[0].contenu:
                    indiceval=t1[0].contenu.index(val)
                    
                    if indiceval == 0 :
                        tj.contenu = [[]] + tj.contenu

                    for k in range(len(t1)):
                        tj.contenu[indiceval].append(t1[k].contenu[indiceval][0])
                            
                    for k in range(len(t2)):
                        tj.contenu[indiceval].append(0)
                            
                    if indiceval != 0 :
                        ind_upt1=indiceval-1
                        upt1=t1[0].contenu[ind_upt1][0]
                        ind_uptj = ind_upt1
                        uptj=tj.contenu[ind_uptj][0]
                        
                        while upt1 != uptj :
                            ind_uptj += 1
                            uptj = tj.contenu[ind_uptj][0]
                        
                        while uptj == tj.contenu[ind_uptj +1][0] :
                            ind_uptj += 1 
                            uptj = tj.contenu[ind_uptj][0]

                        for k in range(len(t1)-1):
                            tj.contenu[ind_uptj+1].append(t1[k+1].contenu[indiceval][0])
                            
                        for k in range(len(t2)-1):
                            tj.contenu[ind_uptj+1].append(0)
                            
        return tj





