#from TransformationAbstraite import TransformationAbstraite
#from EstimateurMoyenne import EstimateurMoyenne

class TransformationMoyenneglissante():
    def __init__(self,periode,nomcolonnes):
        self.periode=periode
        self.nomcolonnes=nomcolonnes
    

    def transform(self,table):
        ''' pq on a code, paramètre, but de la fonction, resultat'''
        """
        transform(self, table)

                Retourne la table originale avec une nouvelle variable "Moyenne glissante.." qui contient 
                la moyenne glissante de la table ou les tables données en argument.
                
                Lorsque la table donnée en argument contient des variables qualitatives à plusieurs modalités
                on commmence par créer des nouvelles tables qui différencie chaque modalité. Par exemple, qi dans la table il y a les différents 
                départements, on aura une liste de table contenant autant de table que chaque département et elle ne contiendra les données que 
                pour le département voulu. C'est le but des fonctions selection_modalite et tables_par_modalites.
                

                Paramètres
                ----------
                table : Table
                    Table donnée en argument sur laquelle on veut calculer la/les moyennes glissantes

                Returns
                -------
                liste_tables : liste de Table
                    liste des tables (s'il y en a plusieurs ie dans le cas où on a une variable qualitative 
                    à plusieurs modalités dans la table de départ) auquel on a ajouté une colonne contenant
                    la moyenne glissante
        """
        # Etape 1 : Créer différentes tables suivant les modalités des variables qualitatives (ex: ) d'où la création de selection-modalite() et tables_par_modalites()
        def selection_modalite(nomcol,modalite,table):
             indice=table.colonnes.index(nomcol)
             nb_obs=len(table.contenu)
             for ligne in range (nb_obs):
                if  table.contenu[ligne][indice]!=modalite:
                      table.enlevlig(ligne)
    
    
        def tables_par_modalites(liste_col,table):
            for col in liste_col:
                indice = table.colonnes.index(col)
                liste_modalites=[]
                nb_obs=len(table.contenu)
                for ligne in range(nb_obs):
                    if table.contenu[ligne][indice] not in liste_modalites:
                        liste_modalites.append(table.contenu[ligne][indice])
                liste_tables=[]
                for modalite in liste_modalites:
                    copie_table=table
                    a=selection_modalite(col,modalite,copie_table)
                    liste_tables.append(a)
            return(liste_tables)
    
    
        def fusionne_tables(liste_tables):
            table_fusionnee=liste_tables[0]
            for table in liste_tables[1:]:
                for ligne in table:
                    table_fusionnee.ajoutlig(ligne)
            return(table_fusionnee)

        # Etape 2: Pour chaque table et chaque colonne sur lesquels on veut avoir la moyenne glissante on l'a fait et on l'ajoute dans notre table
        liste_tables=tables_par_modalites(self.nomcolonnes,table)
        for table in liste_tables:
            longueurtable=len(table)
            for ligne in range (longueurtable-self.periode):
                moyenneglissante=[None for k in range(self.periode-1)]
                for nomcol in table.nomcolonnes:
                    moyenne=EstimateurMoyenne.moyenne(table[ligne:ligne+self.periode-1],nomcol)
                    moyenneglissante.append(moyenne)
                    table.ajoutcol('Moyenne_glissante sur {} jours de {}'.format(self.periode,nomcol),moyenne)
        # Etape 3: On fusionne les différentes tables afin de retourner une seule et unique table  
        return(fusionne_tables(liste_tables))




