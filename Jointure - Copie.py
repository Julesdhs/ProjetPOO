class Jointure :
    def __init__(self, table2, nomcol):
        self.table2=table2
        self.nomcol=nomcol
        
    def transforme(self,table1):
        n=len(table1.contenu)
        p=len(table1.colonnes)
        q=len(self.table2.colonnes)
        #On va créer deux dictionnaire
        #Dictionnaire gauche aura comme clé l'ensemble des valeurs qui sont dans nomcol pour la table1
        #Et aura pour valeur les positions d'apparition pour cette clé
        #Et de même pour Dictionnaire droit
        Dictionnaire_gauche={}
        
        U=[]
        V=[]
        j=table1.colonnes.index(self.nomcol)
        s=self.table2.colonnes.index(self.nomcol)
        for i in range (0, n):
            U.append(table1.contenu[i][j])
        for i in range (0, len(self.table2.contenu)):
            V.append(self.table2.contenu[i][s])
        
        #U=SelectionVariablecsv.transforme(SelectionVariablecsv(table1, self.nomcol))
        
        for k in range(0,n):
            if U[k][0] in Dictionnaire_gauche:
                Dictionnaire_gauche[U[k]].append(k)
            else:
                Dictionnaire_gauche[U[k]]=[k]
        
        Dictionnaire_droit={}
        #V=SelectionVariablecsv.transforme(SelectionVariablecsv(self.table2, self.nomcol))
        for k in range(0,n):
            if V[k] in Dictionnaire_droit:
                Dictionnaire_droit[V[k]].append(k)
            else:
                Dictionnaire_droit[V[k]]=[k]
        
        #On crée la table finale
        #Pour le moment c'est un element vide de la la classe Donnees
        Table_j=Table([],[[]])
        Table_j.colonnes=[None]*(p+q)
        #On commence par remplir Table_j en mettant le nom des variable
        L=[table1.colonnes[k] for k in range(len(table1.colonnes))]
        L+=["{}".format(variable) for variable in self.table2.colonnes]
                
        for k in range (0,p+q):
            Table_j.colonnes[k]="{}".format(L[k])
            
        #On continue de remplir Table_j en mettant les clé autant de fois qu'elles doivent apparaitre
        for cle in Dictionnaire_gauche:
            apparition=len(Dictionnaire_gauche[cle])
            if cle in Dictionnaire_droit:
                apparition+=len(Dictionnaire_droit[cle])-1
            for i in range(apparition):
                L=['NULL' for k in range(p+q)]
                L[0]=cle
                Table_j.ajoutlig(L)
        Table_j.enlevlig(1)
        
        #On continue de remplir Table_j avec toute la partie gauche
        for k in range(len(Table_j.contenu)):
            
            A=table1.contenu[U.index(Table_j.contenu[k][0])][:j] #j est l'indice où se trouve la cle dans la table1
            A+=table1.contenu[U.index(Table_j.contenu[k][0])][j+1:]
            for _ in range(0,q):
                A.append('NULL')
            Table_j.contenu[k][1:]=A
            
        #Enfin on remplit la partie droite quand il y'a bien une relation
        W=[]
        h=Table_j.colonnes.index(self.nomcol)
        for i in range (0, n):
            W.append(Table_j.contenu[i][h])
        
        for cle in Dictionnaire_gauche:
            if cle in Dictionnaire_droit:
                i=0
                for position in Dictionnaire_droit[cle]:
                    B=self.table2.contenu[position][:s]
                    B+=self.table2.contenu[position][s+1:]
                    Table_j.contenu[W.index(cle)+i][p:]=B
                    i+=1
        
        return(Table_j)