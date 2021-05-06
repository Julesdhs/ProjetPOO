from TransformationAsbtraite import TransformationAbstraite


class TransformationSpatiale(TransformationAbstraite):
      '''les données sont indexées par région ou département : les méthodes ici vont permettre de passer d'une granularité départementale à régionale ou nationale

      L'attribut correspondra à l'espace de départ et on implémentera une méthode pour l'agrégation

      L'espace de départ s'adaptera aux données du tableau considéré, si les données sont ordonnées par région alors espace_depart sera initialisé à 1 autrement il sera initialisé à 0 (département)

      L'espace final sera un entier, soit 1 ou 2 pour l'agrégation respective régionale ou nationale;

        '''
      def __init__(table,espace_depart='problemetableau',espace_final):
            if dep in table.colonnes :
                 espace_depart = 0
            if numreg or reg in table.colonnes :
                  espace_depart = 1
            self.espace_depart = espace_depart
            self.espace_final = espace_final

      def transform(self,table):
            ''' on crée un dictionnaire des régions composées de leurs départements ; les régions sont ici les numéros que l'on retrouve dans les variables numreg '''

            dic = {1:[971],2:[972],3:[973],4:[974],6:[976],11:[75,77,78,91,92,93,94,95],24:[18,28,36,37,41,45],27:[21,25,39,58,70,71,89,90],28:[14,27,50,61,76],32:[2,59,60,62,80],44:[8,10,51,52,54,55,57,67,68,88],52:[44,49,53,72,85],53:[22,29,35,56],75:[16,17,19,23,24,33,40,47,64,79,86,87],76:[9,11,12,30,31,32,34,46,48,65,66,81,82],84:[1,3,7,15,26,38,42,43,63,69,73,74], 93: [4,5,6,13,83,84],94:[2]}

        ''' premier cas : l'espace de départ possède une granularité départementale ; on va passer à une granularité régionale
           La variable jour est présente dans toutes les données, mais aussi il y a la variable sexe dans certaines '''

            if self.espace_depart == 0 :
                  if self.espace_final == 1:
            ''' on va d'abord grouper par la variable sexe si elle existe puis par le jour qui lui est présent dans toutes les tables : on considère que les tables que nous mnipulerons auront forcément une variable jour et au maximum une variable sexe en qualitative'''
                      var = table.colonnes
                      if sexe in var :
                            indsexe =  table.colonnes.index(sexe)
                            inddep  =  table.colonnes.index(dep)
                            indjour =  table.colonnes.index(jour)
                            newt = Table()
                            newt.colonnes = table.colonnes
                            newt.colonnes[inddep]= reg
                            nbjours = len(table.contenu)//300
                            ''' on va créer une nouvelle table en regroupant en fonction des régions, il faut cependant prendre en compte les modalités des variables sexe et jour'''
                            for c in range(nbjours):
                                jour = table.contenu[300*c][indjour]
                                for j in dic.items():
                        ,           ligne0 = [0 for k in range(len(var))]
                                    ligne1 = [0 for k in range(len(var))]
                                    ligne2 = [0 for k in range(len(var))]
                                    ligne0[inddep]=j[0]
                                    ligne1[inddep]=j[0]
                                    ligne2[inddep]=j[0]
                                    ligne0[indjour]= jour
                                    ligne1[indjour]= jour
                                    ligne2[indjour]= jour
                                    departements = j[1]
                                    for i in range(100):
                                        if table.contenu[300*c + i][inddep] in departements:
                                              for j in range(len(var)):
                                                    if j!= inddep and j!= indjour and j!= indsexe :
                                                          if table.contenu[300*c + i][indsexe] == 0:
                                                                ligne0[j]+= table.contenu[300*c + i][j]
                                                          if table.contenu[300*c + i][indsexe] == 1:
                                                                ligne1[j]+= table.contenu[300*c + i][j]
                                                          if table.contenu[300*c + i][indsexe] == 2:
                                                                ligne2[j]+= table.contenu[300*c + i][j]
                                    newt.ajoutlig(ligne0)
                                    newt.ajoutlig(ligne1)
                                    newt.ajoutlig(ligne2)
                       else:
                            inddep  =  table.colonnes.index(dep)
                            indjour =  table.colonnes.index(jour)
                            newt = Table()
                            newt.colonnes = table.colonnes
                            newt.colonnes[inddep]= reg
                            nbjours = len(table.contenu)//3
                            for c in range(nbjours):
                                jour = table.contenu[300*c][indjour]
                                for j in dic.items():
                        ,           ligne = [0 for k in range(len(var))]]
                                    ligne[inddep]=j[0]
                                    ligne[indjour]= jour
                                    departements = j[1]
                                    for i in range(100):
                                        if table.contenu[300*c + i][inddep] in departements:
                                              for j in range(len(var)):
                                                    if j!= inddep and j!= indjour :
                                                        ligne0[j]+= table.contenu[300*c + i][j]
                                    newt.ajoutlig(ligne)
                  if self.espace_final == 2:
                  ''' le code est le même que celui précédent juste que l'on va maintenant rajouter le passage de newt à un tableau à granularité nationale (ou on somme tout en quelque sorte) '''
                      var = table.colonnes
                      if sexe in var :
                            indsexe =  table.colonnes.index(sexe)
                            inddep  =  table.colonnes.index(dep)
                            indjour =  table.colonnes.index(jour)
                            newt = Table()
                            newt.colonnes = table.colonnes
                            newt.colonnes[inddep]= reg
                            nbjours = len(table.contenu)//3
                            for c in range(nbjours):
                                jour = table.contenu[300*c][indjour]
                                for j in dic.items():
                        ,           ligne0 = [0 for k in range(len(var))]
                                    ligne1 = [0 for k in range(len(var))]
                                    ligne2 = [0 for k in range(len(var))]
                                    ligne0[inddep]=j[0]
                                    ligne1[inddep]=j[0]
                                    ligne2[inddep]=j[0]
                                    ligne0[indjour]= jour
                                    ligne1[indjour]= jour
                                    ligne2[indjour]= jour
                                    ligne1[indsexe] = 1
                                    ligne2[indsexe] = 2
                                    departements = j[1]
                                    for i in range(100):
                                        if table.contenu[300*c + i][inddep] in departements:
                                              for j in range(len(var)):
                                                    if j!= inddep and j!= indjour and j!= indsexe :
                                                          if table.contenu[300*c + i][indsexe] == 0:
                                                                ligne0[j]+= table.contenu[300*c + i][j]
                                                          if table.contenu[300*c + i][indsexe] == 1:
                                                                ligne1[j]+= table.contenu[300*c + i][j]
                                                          if table.contenu[300*c + i][indsexe] == 2:
                                                                ligne2[j]+= table.contenu[300*c + i][j]
                                    newt.ajoutlig(ligne0)
                                    newt.ajoutlig(ligne1)
                                    newt.ajoutlig(ligne2)
                       else:
                            inddep  =  table.colonnes.index(dep)
                            indjour =  table.colonnes.index(jour)
                            newt = Table()
                            newt.colonnes = table.colonnes
                            newt.colonnes[inddep]= reg
                            nbjours = len(table.contenu)//3
                            for c in range(nbjours):
                                jour = table.contenu[300*c][indjour]
                                for j in dic.items():
                        ,           ligne = [0 for k in range(len(var))]]
                                    ligne[inddep]=j[0]
                                    ligne[indjour]= jour
                                    departements = j[1]
                                    for i in range(100):
                                        if table.contenu[300*c + i][inddep] in departements:
                                              for j in range(len(var)):
                                                    if j!= inddep and j!= indjour :
                                                        ligne[j]+= table.contenu[300*c + i][j]
                                    newt.ajoutlig(ligne)
            else:
                  if self.espace_depart == 1:
                        if self.espace_final == 2:
                              var = table.colonnes
                              if cl_age90 in var:
                                   indage=  table.colonnes.index(cl_age90)
                                   indreg  =  table.colonnes.index(reg)
                                   indjour =  table.colonnes.index(jour)
                                   newt = Table()
                                   newt.colonnes = table.colonnes
                                   newt.colonnes[indreg]= nat
                                   nbjours = len(table.contenu)//1100
                                   for c in range(nbjours):
                                       jour = table.contenu[1100*c][indjour]
                                       ligne0 = [0 for k in range(len(var))]
                                       ligne9 = [0 for k in range(len(var))]
                                       ligne19 = [0 for k in range(len(var))]
                                       ligne29 = [0 for k in range(len(var))]
                                       ligne39 = [0 for k in range(len(var))]
                                       ligne49 = [0 for k in range(len(var))]
                                       ligne59 = [0 for k in range(len(var))]
                                       ligne69 = [0 for k in range(len(var))]
                                       ligne79 = [0 for k in range(len(var))]
                                       ligne89 = [0 for k in range(len(var))]
                                       ligne90 = [0 for k in range(len(var))]
                                       ligne0[indreg] = 'nat'
                                       ligne0[indjour] = jour
                                       ligne9[indreg] = 'nat'
                                       ligne9[indjour] = jour
                                       ligne19[indreg] = 'nat'
                                       ligne19[indjour] = jour
                                       ligne29[indreg] = 'nat'
                                       ligne29[indjour] = jour
                                       ligne39[indreg] = 'nat'
                                       ligne39[indjour] = jour
                                       ligne49[indreg] = 'nat'
                                       ligne49[indjour] = jour
                                       ligne59[indreg] = 'nat'
                                       ligne59[indjour] = jour
                                       ligne69[indreg] = 'nat'
                                       ligne69[indjour] = jour
                                       ligne79[indreg] = 'nat'
                                       ligne79[indjour] = jour
                                       ligne89[indreg] = 'nat'
                                       ligne89[indjour] = jour
                                       ligne90[indreg] = 'nat'
                                       ligne90[indjour] = jour
                                       for i in range(1100):
                                             for j in range(len(var)):
                                                if j!= indreg and j!= indjour :
                                                   if table.contenu[1100*c +i][indage]== 0:
                                                         ligne0[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 9:
                                                         ligne9[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 19:
                                                         ligne19[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 29:
                                                         ligne29[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 39:
                                                         ligne39[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 49:
                                                         ligne49[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 59:
                                                         ligne59[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 69:
                                                         ligne69[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 79:
                                                         ligne79[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 89:
                                                         ligne89[j]+= table.contenu[1100*c + i]
                                                   if table.contenu[1100*c +i][indage]== 90:
                                                         ligne90[j]+= table.contenu[1100*c + i]
                                       newt.ajoutlig(ligne0)
                                       newt.ajoutlig(ligne9)
                                       newt.ajoutlig(ligne19)
                                       newt.ajoutlig(ligne29)
                                       newt.ajoutlig(ligne39)
                                       newt.ajoutlig(ligne49)
                                       newt.ajoutlig(ligne59)
                                       newt.ajoutlig(ligne69)
                                       newt.ajoutlig(ligne79)
                                       newt.ajoutlig(ligne89)
                                       newt.ajoutlig(ligne90)

















''' code non terminé : il reste encore le cas ou il y a pas la variable classe mais la variable num_reg  ;
il reste aussi de compléter le passage de région à nation lors du cas 0 -> 2 '''






































