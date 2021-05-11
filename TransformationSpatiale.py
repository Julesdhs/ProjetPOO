#from TransformationAsbtraite import TransformationAbstraite


class TransformationSpatiale(TransformationAbstraite):
      '''les données sont indexées par région ou département : les méthodes ici vont permettre de passer d'une granularité départementale à régionale ou nationale

      L'attribut correspondra à l'espace de départ et on implémentera une méthode pour l'agrégation

      L'espace de départ s'adaptera aux données du tableau considéré, si les données sont ordonnées par région alors espace_depart sera initialisé à 1 autrement il sera initialisé à 0 (département)

      L'espace final sera un entier, soit 1 ou 2 pour l'agrégation respective régionale ou nationale'''

      def __init__(self,espace_final,espace_depart=2):
            self.espace_depart = espace_depart
            self.espace_final = espace_final

      def transform(self,table):
            ''' on crée un dictionnaire des régions composées de leurs départements ; les régions sont ici les numéros que l'on retrouve dans les variables numreg '''

            dic = {'Guadeloupe':['971'],'Martinique':['972'],'Guyane':['973'],'La Réunion':['974'],'Mayotte':['976'],'Île-de-france':['75','77','78','91','92','93','94','95'],'Centre Val de Loire':['18','28','36','37','41','45'],'Bourgogne-Franche-Compté':['21','25','39','58','70','71','89','90'],'Normandie':['14','27','50','61','76'],'Picardie':['2','59','60','62','80'],'Grand Est':['8','10','51','52','54','55','57','67','68','88'],'Loire-Atlantique':['44','49','53','72','85'],'Bretagne':['22','29','35','56'],'Nouvelle-Aquitaine':['16','17','19','23','24','33','40','47','64','79','86','87'],'Occitanie':['9','11','12','30','31','32','34','46','48','65','66','81','82'],'Auvergne-Rhône-Alpes':['1','3','7','15','26','38','42','43','63','69','73','74'], 'Provence-Alpes-Côte dazur':['4','5','6','13','83','84'],'Corse':['2A','2B']}

            ''' premier cas : l'espace de départ possède une granularité départementale ; on va passer à une granularité régionale
           La variable jour est présente dans toutes les données, mais aussi il y a la variable sexe dans certaines '''

            if self.espace_depart == 0 :
                  if self.espace_final == 1:
                        ''' on va d'abord grouper par la variable sexe si elle existe puis par le jour qui lui est présent dans toutes les tables : on considère que les tables que nous mnipulerons auront forcément une variable jour et au maximum une variable sexe en qualitative'''
                        var = table.colonnes
                        if 'sexe' in var :
                              indsexe =  table.colonnes.index('sexe')
                              inddep  =  table.colonnes.index('dep')
                              indjour =  table.colonnes.index('jour')
                              newt = Table()
                              newt.colonnes = table.colonnes
                              newt.colonnes[inddep]= 'reg'
                              nbjours = len(table.contenu)//303
                              ''' on va créer une nouvelle table en regroupant en fonction des régions, il faut cependant prendre en compte les modalités des variables sexe et jour'''
                              for c in range(nbjours):
                                    jour = table.contenu[303*c][indjour]
                                    for j in dic.items():
                                          ligne0 = [0 for k in range(len(var))]
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
                                          for i in range(303):
                                                if table.contenu[303*c + i][inddep] in departements:
                                                      for j in range(len(var)):
                                                            if j!= inddep and j!= indjour and j!= indsexe :
                                                                  if table.contenu[303*c + i][indsexe] == '0':
                                                                        ligne0[j]+= table.contenu[303*c + i][j]
                                                                  if table.contenu[303*c + i][indsexe] == '1':
                                                                        ligne1[j]+= table.contenu[303*c + i][j]
                                                                  if table.contenu[303*c + i][indsexe] == '2':
                                                                        ligne2[j]+= table.contenu[303*c + i][j]
                                          newt.ajoutlig(ligne0)
                                          newt.ajoutlig(ligne1)
                                          newt.ajoutlig(ligne2)
                              table.colonnes = newt.colonnes
                              table.contenu = newt.contenu
                        else:
                              inddep  =  table.colonnes.index('dep')
                              indjour =  table.colonnes.index('jour')
                              newt = Table()
                              newt.colonnes = table.colonnes
                              newt.colonnes[inddep]= 'reg'
                              nbjours = len(table.contenu)//101
                              for c in range(nbjours):
                                    jour = table.contenu[101*c][indjour]
                                    for j in dic.items():
                                          ligne = [0 for k in range(len(var))]
                                          ligne[inddep]=j[0]
                                          ligne[indjour]= jour
                                          departements = j[1]
                                          for i in range(101):
                                                if table.contenu[101*c + i][inddep] in departements:
                                                      for j in range(len(var)):
                                                            if j!= inddep and j!= indjour :
                                                                ligne[j]+= table.contenu[101*c + i][j]
                                          print(ligne)
                                          newt.ajoutlig(ligne)
                              table.colonnes = newt.colonnes
                              table.contenu = newt.contenu
                  if self.espace_final == 2:
                        ''' le code est le même que celui précédent juste que l'on va maintenant rajouter le passage de newt à un tableau à granularité nationale (ou on somme tout en quelque sorte) '''
                        var = table.colonnes
                        if 'sexe' in var :
                              indsexe =  table.colonnes.index('sexe')
                              inddep  =  table.colonnes.index('dep')
                              indjour =  table.colonnes.index('jour')
                              newt = Table()
                              newt.colonnes = table.colonnes
                              newt.colonnes[inddep] = 'reg'
                              nbjours = len(table.contenu)//303
                              for c in range(nbjours):
                                    jour = table.contenu[303*c][indjour]
                                    for j in dic.items():
                                          ligne0 = [0 for k in range(len(var))]
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
                                    for i in range(101):
                                          if table.contenu[300*c + i][inddep] in departements:
                                                for v in range(len(var)):
                                                      if (v!= inddep and v!= indjour and v!= indsexe) :
                                                            if table.contenu[303*c + i][indsexe] == '0':
                                                                  ligne0[v]+= table.contenu[303*c + i][v]
                                                            elif table.contenu[303*c + i][indsexe] == '1':
                                                                  ligne1[v]+= table.contenu[303*c + i][v]
                                                            elif table.contenu[303*c + i][indsexe] == '2':
                                                                  ligne2[v]+= table.contenu[303*c + i][v]
                                    newt.ajoutlig(ligne0)
                                    newt.ajoutlig(ligne1)
                                    newt.ajoutlig(ligne2)
                              nbjours = len(newt.contenu)//18*3
                              indnom = newt.colonnes.index(nom_reg)
                              newt2 = Table()
                              newt2.colonnes = table.colonnes
                              indreg  =  newt.colonnes.index('reg')
                              newt2.colonnes[indreg] = nat
                              indjour =  newt.colonnes.index('jour')
                              indsexe = newt.colonnes.index('sexe')
                              for c in range(nbjours):
                                    jour = newt.contenu[18*3*c][indjour]
                                    ligne0 = [0 for k in range(len(table.colonnes))]
                                    ligne1 = [0 for k in range(len(table.colonnes))]
                                    ligne2 = [0 for k in range(len(table.colonnes))]
                                    ligne0[indjour] = jour
                                    ligne0[indreg] = 'France'
                                    ligne1[indjour] = jour
                                    ligne1[indreg] = 'France'
                                    ligne2[indjour] = jour
                                    ligne2[indreg] = 'France'
                                    ligne1[indsexe] = 1
                                    ligne2[indsexe] = 2
                                    for i in range(18):
                                          for j in range(len(table.colonnes)):
                                                if j!= indreg and j!= indjour:
                                                      if newt.contenu[18*c + i][indsexe]== 0:
                                                            ligne0[j]+= table.contenu[3*18*c + i]
                                                      elif newt.contenu[18*c + i][indsexe]== 1:
                                                            ligne1[j]+= table.contenu[3*18*c + i]
                                                      elif newt.contenu[18*c + i][indsexe]==2:
                                                            ligne2[j]+= table.contenu[3*18*c + i]
                                    newt2.ajoutlig(ligne0)
                                    newt2.ajoutlig(ligne1)
                                    newt2.ajoutlig(ligne2)
                              table.colonnes = newt2.colonnes
                              table.contenu = newt2.contenu
                        else:
                              inddep  =  table.colonnes.index('dep')
                              indjour =  table.colonnes.index('jour')
                              newt = Table()
                              newt.colonnes = table.colonnes
                              newt.colonnes[inddep]= 'reg'
                              nbjours = len(table.contenu)//101
                              for c in range(nbjours):
                                    jour = table.contenu[101*c][indjour]
                                    for j in dic.items():
                                          ligne = [0 for k in range(len(var))]
                                          ligne[inddep]=j[0]
                                          ligne[indjour]= jour
                                          departements = j[1]
                                          for i in range(101):
                                                if table.contenu[101*c + i][inddep] in departements:
                                                      for j in range(len(var)):
                                                            if j!= inddep and j!= indjour :
                                                                ligne[j]+= table.contenu[101*c + i][j]
                                          newt.ajoutlig(ligne)
                              table.colonnes = newt.colonnes
                              table.contenu = newt.contenu

                              nbjours = len(newt.contenu)//18
                              print(nbjours)
                              newt2 = Table()
                              newt2.colonnes = newt.colonnes
                              indreg  =  newt.colonnes.index('reg')
                              newt2.colonnes[indreg] = 'France'
                              newt2.colonnes[indreg] = 'France'
                              indjour =  newt.colonnes.index('jour')
                              for p in range(nbjours):
                                    print(p)
                                    jour = newt.contenu[18*p][indjour]
                                    ligne = [0 for k in range(len(table.colonnes))]
                                    ligne[indjour] = jour
                                    ligne[indreg] = 'France'
                                    for i in range(18):
                                          for j in range(len(table.colonnes)):
                                                if j!= indreg and j!= indjour:
                                                      ligne[j]+= table.contenu[18*c + i][j]
                                    newt2.ajoutlig(ligne)
                              table.colonnes = newt2.colonnes
                              table.contenu = newt2.contenu
            else:
                  ''' ici c'est le cas où nous commençons d'une granularité régionale pour aller à une nationale, on regarde d'abord si la variable classe d'âge est présente pour séparer en fonction de ses modalités'''
                  if self.espace_depart == 1:
                        if self.espace_final == 2:
                              var = table.colonnes
                              if 'cl_age90' in var:
                                    indage=  table.colonnes.index('cl_age90')
                                    indreg  =  table.colonnes.index('reg')
                                    indjour =  table.colonnes.index('jour')
                                    newt = Table()
                                    newt.colonnes = table.colonnes
                                    newt.colonnes[indreg]= nat
                                    nbjours = len(table.contenu)//(11*18)
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
                                          ligne0[indreg] = 'France'
                                          ligne0[indjour] = jour
                                          ligne9[indreg] = 'France'
                                          ligne9[indjour] = jour
                                          ligne19[indreg] = 'France'
                                          ligne19[indjour] = jour
                                          ligne29[indreg] = 'France'
                                          ligne29[indjour] = jour
                                          ligne39[indreg] = 'France'
                                          ligne39[indjour] = jour
                                          ligne49[indreg] = 'France'
                                          ligne49[indjour] = jour
                                          ligne59[indreg] = 'France'
                                          ligne59[indjour] = jour
                                          ligne69[indreg] = 'France'
                                          ligne69[indjour] = jour
                                          ligne79[indreg] = 'France'
                                          ligne79[indjour] = jour
                                          ligne89[indreg] = 'France'
                                          ligne89[indjour] = jour
                                          ligne90[indreg] = 'France'
                                          ligne90[indjour] = jour
                                          for i in range(11*18):
                                                for j in range(len(var)):
                                                      if j!= indreg and j!= indjour :
                                                            if table.contenu[11*18*c +i][indage]== 0:
                                                                  ligne0[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 9:
                                                            ligne9[j]+= table.contenu[11*c*18 + i]
                                                      elif table.contenu[11*18*c +i][indage]== 19:
                                                            ligne19[j]+= table.contenu[11*c*18 + i]
                                                      elif table.contenu[11*18*c +i][indage]== 29:
                                                            ligne29[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 39:
                                                            ligne39[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 49:
                                                            ligne49[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 59:
                                                            ligne59[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 69:
                                                            ligne69[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 79:
                                                            ligne79[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 89:
                                                            ligne89[j]+= table.contenu[11*18*c + i]
                                                      elif table.contenu[11*18*c +i][indage]== 90:
                                                            ligne90[j]+= table.contenu[11*18*c + i]
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
                                    table.colonnes = newt.colonnes
                                    table.contenu = newt.contenu


                              elif 'nomReg'in var:
                                    nbjours = len(table.contenu)//18
                                    indnom = table.colonnes.index('nomReg')
                                    indreg  =  table.colonnes.index('numReg')
                                    newt = Table()
                                    newt.colonnes = table.colonnes
                                    newt.colonnes[indreg] = 'nat'
                                    indjour =  table.colonnes.index('jour')
                                    table.enlevcol(indnom)
                                    for c in range(nbjours):
                                          jour = table.contenu[18*c][indjour]
                                          ligne = [0 for k in range(len(table.colonnes))]
                                          ligne[indjour] = jour
                                          ligne[indreg] = 'France'
                                          for i in range(18):
                                                for j in range(len(table.colonnes)):
                                                      if j!= indreg and j!= indjour and j!= indnom :
                                                            ligne[j]+= table.contenu[18*c + i][j]
                                          newt.ajoutlig(ligne)
                                    table.colonnes = newt.colonnes
                                    table.contenu = newt.contenu

































































