class TransformationJointure(TransformationAbstraite) :
    '''
    Attributs
    ----------
    table2 : table
        une table qu'on joint à la table en argument de transform
    
    nomcol : str
        la colonne clé de la jointure
        
    Méthodes
    -------
    transform()
        applique la jointure à la table en argument

    '''

    def __init__(self, table2, nomcol):
        self.table2=table2
        self.nomcol=nomcol
        
    def transform(self,table1):
        n=len(table1.contenu)
        p=len(table1.colonnes)
        q=len(self.table2.colonnes)
        '''
        On crée deux dictionnaires ayant chacun comme clefs les valeurs qui sont dans la clé primaires pour la table1 et aura pour valeur les positions d'apparition des clefs
        '''
        Dictionnaire_gauche={}
        
        U=[]
        V=[]
        j=table1.colonnes.index(self.nomcol)
        s=self.table2.colonnes.index(self.nomcol)
        for i in range (0, n):
            U.append(table1.contenu[i][j])
        for i in range (0, len(self.table2.contenu)):
            V.append(self.table2.contenu[i][s])
        
        for k in range(0,n):
            if U[k][0] in Dictionnaire_gauche:
                Dictionnaire_gauche[U[k]].append(k)
            else:
                Dictionnaire_gauche[U[k]]=[k]
        
        Dictionnaire_droit={}
    
        for k in range(0,n):
            if V[k] in Dictionnaire_droit:
                Dictionnaire_droit[V[k]].append(k)
            else:
                Dictionnaire_droit[V[k]]=[k]
        
        
        Table_j=Table([],[[]])
        
        Table_j.colonnes=[table1.colonnes[k] for k in range(len(table1.colonnes))]
        Table_j.colonnes+=[self.table2.colonnes[k] for k in range(len(self.table2.colonnes)) if self.table2.colonnes[k] not in table1.colonnes]
                
        
        ''''    
        On remplit Table_j en mettant les clefs autant de fois qu'elles doivent apparaitre
        '''
        for clef in Dictionnaire_gauche:
            apparition=len(Dictionnaire_gauche[clef])
            if clef in Dictionnaire_droit:
                apparition+=len(Dictionnaire_droit[clef])-1
            for i in range(apparition):
                L=['NULL' for k in range(p+q)]
                L[0]=clef
                Table_j.ajoutlig(L)
        Table_j.enlevlig(1)
        '''
        On continue de remplir Table_j avec toute la partie gauche
        '''
        for k in range(len(Table_j.contenu)):
            
            A=table1.contenu[U.index(Table_j.contenu[k][0])][:j] 
            '''
            j est l'indice où se trouve la clef dans la table1
            '''
            A+=table1.contenu[U.index(Table_j.contenu[k][0])][j+1:]
            for _ in range(0,q):
                A.append('NULL')
            Table_j.contenu[k][1:]=A
        '''
        Pour finir on remplit la partie droite quand il y'a bien une relation
        '''
        W=[]
        h=Table_j.colonnes.index(self.nomcol)
        for i in range (0, n):
            W.append(Table_j.contenu[i][h])
        
        for clef in Dictionnaire_gauche:
            if clef in Dictionnaire_droit:
                i=0
                for position in Dictionnaire_droit[clef]:
                    B=self.table2.contenu[position][:s]
                    '''
                    s est l'indice de la colonne clé dans la table 2
                    '''
                    B+=self.table2.contenu[position][s+1:]
                    Table_j.contenu[W.index(clef)+i][p:]=B
                    i+=1
        
        table1.colonnes = []
        table1.contenu = [[Table_j.contenu][0] for k in range(len(Table_j.contenu))]
        print(Table_j.colonnes,Table_j.contenu[0])
        print(len(Table_j.contenu),len(table1.contenu))
        for j in range(len(Table_j.colonnes)) :
            table1.colonnes.append(Table_j.colonnes[j])
        for k in range(len(Table_j.contenu)):
                for j in range(1,len(Table_j.colonnes)):
                    table1.contenu[k].append(Table_j.contenu[k][j])
                    
        
        