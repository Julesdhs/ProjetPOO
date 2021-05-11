

class TransformationSelectionVariables(TransformationAbstraite):
    def __init__(self,variables = []):
        self.variables = variables



    def transform(self,table):

          ''' on crée la liste d'indices associées à la liste des variables ; ensuite on enlève les colonnes des variables dont les indices ne sont pas dans la liste '''

          listind = []
          for x in self.variables :
            listind.append(table.colonnes.index(x))
          n = len(table.contenu[0])
          for c in reversed(range(n)):
              if c not in listind :
                  table.enlevcol(c)




###



    def transform(self,table):

          ''' on crée la liste d'indices associées à la liste des variables ; ensuite on enlève les colonnes des variables dont les indices ne sont pas dans la liste '''

          listind = []
          for x in self.variables :
            listind.append(table.colonnes.index(x))
          n = len(table.contenu[0])
          for c in reversed(range(n)):
              if c not in listind :
                  table.enlevcol(c)


    def transform(self,table):
        newt = Table()
        for x in self.variables :
            listind.append((x,table.colonnes.index(x))
        n = len(table.contenu[0])
        for c in (listind[::-1]) :
            for ligne in table.contenu:
                 col.append([ligne[c[1]]])
            ajoutcol(c[0],col)



    def transform(self,table):

          ''' on crée la liste d'indices associées à la liste des variables ; ensuite on enlève les colonnes des variables dont les indices ne sont pas dans la liste '''

          listind = []
          for x in self.variables :
            listind.append(table.colonnes.index(x)-1)
          n = len(table.contenu[0])
          pos = 0
          for c in range(n):
              if c not in listind :
                  table.enlevcol(c-pos)
                  pos +=1


















