from donnees import Donnees
from selectionvariablecsv import SelectionVariablecsv

class Jointure :
    def __init__(self, table1, table2, variable_cle):
        self.table1=table1
        self.table2=table2
        self.variable_cle=variable_cle
        
    def transforme(self):
        n=len(self.table1.lignes)
        p=len(self.table1.noms_colonnes)
        q=len(self.table2.noms_colonnes)
        #On va créer deux dictionnaire
        #Dictionnaire gauche aura comme clé l'ensemble des valeurs qui sont dans variable_cle pour la table1
        #Et aura pour valeur les positions d'apparition pour cette clé
        #Et de même pour Dictionnaire droit
        Dictionnaire_gauche={}
        
        U=[]
        V=[]
        j=self.table1.noms_colonnes.index(self.variable_cle)
        s=self.table2.noms_colonnes.index(self.variable_cle)
        for i in range (0, n):
            U.append(self.table1.lignes[i][j])
        for i in range (0, len(self.table2.lignes)):
            V.append(self.table2.lignes[i][s])
        
        #U=SelectionVariablecsv.transforme(SelectionVariablecsv(self.table1, self.variable_cle))
        
        for k in range(0,n):
            if U[k][0] in Dictionnaire_gauche:
                Dictionnaire_gauche[U[k]].append(k)
            else:
                Dictionnaire_gauche[U[k]]=[k]
        
        Dictionnaire_droit={}
        #V=SelectionVariablecsv.transforme(SelectionVariablecsv(self.table2, self.variable_cle))
        for k in range(0,n):
            if V[k] in Dictionnaire_droit:
                Dictionnaire_droit[V[k]].append(k)
            else:
                Dictionnaire_droit[V[k]]=[k]
        
        #On crée la table finale
        #Pour le moment c'est un element vide de la la classe Donnees
        Table_jointe=Donnees([],[[]])
        Table_jointe.noms_colonnes=[None]*(p+q)
        #On commence par remplir Table_jointe en mettant le nom des variable
        L=["{}".format(variable) for variable in self.table1.noms_colonnes]
        L+=["{}".format(variable) for variable in self.table2.noms_colonnes]
                
        for k in range (0,p+q):
            Table_jointe.noms_colonnes[k]="{}".format(L[k])
            
        #On continue de remplir Table_jointe en mettant les clé autant de fois qu'elles doivent apparaitre
        for cle in Dictionnaire_gauche:
            apparition=len(Dictionnaire_gauche[cle])
            if cle in Dictionnaire_droit:
                apparition+=len(Dictionnaire_droit[cle])-1
            for i in range(apparition):
                L=['NULL' for k in range(p+q)]
                L[0]=cle
                Table_jointe.ajouter_ligne(L)
        Table_jointe.enlever_ligne(-1)
        
        
        
        #On continue de remplir Table_jointe avec toute la partie gauche
        for k in range(len(Table_jointe.lignes)):
            
            A=self.table1.lignes[U.index(Table_jointe.lignes[k][0])][:j] #j est l'indice où se trouve la cle dans la table1
            A+=self.table1.lignes[U.index(Table_jointe.lignes[k][0])][j+1:]
            for _ in range(0,q):
                A.append('NULL')
            Table_jointe.lignes[k][1:]=A
            
        #Enfin on remplit la partie droite quand il y'a bien une relation
        W=[]
        h=Table_jointe.noms_colonnes.index(self.variable_cle)
        for i in range (0, n):
            W.append(Table_jointe.lignes[i][h])
        
        for cle in Dictionnaire_gauche:
            if cle in Dictionnaire_droit:
                i=0
                for position in Dictionnaire_droit[cle]:
                    B=self.table2.lignes[position][:s]
                    B+=self.table2.lignes[position][s+1:]
                    Table_jointe.lignes[W.index(cle)+i][p:]=B
                    i+=1
        
        '''
        for k in range(len(Table_jointe.lignes)):
            if Table_jointe.lignes[k][0] in Dictionnaire_droit:
                for position in Dictionnaire_droit.value(Table_jointe.lignes[k][0])
                    B=self.table2.lignes[V.index(Table_jointe.lignes[k][0])][:s] #s est l'indice où se trouve la cle dans la table1
                    B+=self.table2.lignes[V.index(Table_jointe.lignes[k][0])][s+1:]
                Table_jointe.lignes[k][p:]=B
        '''    
        return(Table_jointe)
    
    '''
    def transforme(self):
        ##Etape 0 : On enregistre quelques variable qui seront utiles
        p=len(self.table1.noms_colonnes)
        q=len(self.table2.noms_colonnes)
        n=len(self.table1.lignes)+1
        
        #Etape 1: On crée une grande table qui sera notre table jointe finale
        #Au debut cette table doit être composé de n ligne car on fait une jointure à gauche
        #Et pour l'instant on veut des "Null" partout sur le tableau.
        Table_jointe=[]
        for i in range (0,n):
            Table_jointe+=[["NULL" for _ in range (0, p+q)]]
            
        #Pour l'instant notre tableau joint est un table de dimension n*(p+q-1) avec que des null partout
        #On va déjà mettre le nom des variables sur la première ligne
        #La seule variable qui n'est pas potentiellement doublé est la variable clé primaire qui permet de faire la jointure
        #C'est à dire que les autres variables peuvent être doublé si elles apparaissent dans les deux tableaux
        
        L=["{}".format(variable) for variable in self.table1.noms_colonnes]
        #for variable in self.table2.noms_colonnes :
        #    if variable!=self.variable_cle:
        L+=["{}".format(variable) for variable in self.table2.noms_colonnes]
                
        for k in range (0,p+q):
            Table_jointe[0][k]="{}".format(L[k])

        
        #Donc pour le moment on a toujours le même tableau avec des "null" partout sauf sur la première ligne où on a les noms de variable
        #On va copier la table de gauche entièrement.
        for i in range (1,n):
            for j in range (0,p):
                Table_jointe[i][j]=self.table1.lignes[i-1][j]
        
        #Etape 2: On cherche dans la table 2 les lignes qui peuvent être jointe à la table 1
        #C'est à dire les lignes de la table 2 ou une composante de la variable_cle apparait aussi dans la table de gauche
        #M et N sont deux listes qui vont enregistrer les indices de ces lignes qui peuvent être jointes
      
        M=[]
        N=[]
        
        #On extrait les colonnes de la variable cle afin de mieux pouvoir comparer
        j=self.table1.noms_colonnes.index(self.variable_cle)
        h=self.table2.noms_colonnes.index(self.variable_cle)
        U=[]
        V=[]
        for i in range (1, n):
            U.append(self.table1.lignes[i-1][j])
        for i in range (1, len(self.table2.lignes)+1):
            V.append(self.table2.lignes[i-1][h])
        
        for pose_individu,individu in enumerate(V):
            if individu in U:
                M.append(U.index(individu))
                N.append(pose_individu)
        print(U)
        print(V)
        print(M)
        print(N)
                
        #On sait à quel endroit se trouvent les lignes qui peuvent être jointe, il suffit maintenant
        #de recopier dans la grande table finale, les lignes qui peuvent être jointe
        data=Donnees(Table_jointe[0],Table_jointe[1:])
        
        Position_doublons=[]
        Occurence=[]
        for element in M:
            if element not in Position_doublons:
                Position_doublons.append(element)
                Occurence.append(M.count(element))
        
        
        
        #new=['NULL' for k in range(p+q)]
        
        
        for k in range(Occurence[0]-1):
            data.ajouter_ligne(Table_jointe[Position_doublons[0]+1], Position_doublons[0])
        
        decalage=Occurence[0]-1
        
        for k in range (1, len(Position_doublons)):
            for h in range(Occurence[k]-1):
                data.ajouter_ligne(Table_jointe[Position_doublons[k]+1], Position_doublons[k]+decalage)
            decalage+=Occurence[k]
            
        
        
        
        for k in range (0,len(M)):
            for nom_variable in L[p:]:
                s=data.noms_colonnes[p:].index(nom_variable)
                t=self.table2.noms_colonnes.index(nom_variable)
                if 
                
                
                if data.lignes[M[k]][s+p]=='NULL':
                    data.lignes[M[k]][s+p] = self.table2.lignes[N[k]][t]
                #else :
                #    new=['NULL' for k in range(p+q)]
                #    data.ajouter_ligne(new,M[k]+1)
                #    data.lignes[M[k]+1][s+p] = self.table2.lignes[N[k]][t]
                #    for z in range (0, p):
                #        data.lignes[M[k]+1][z]=self.table1.lignes[M[k]][z]
        return data
    '''