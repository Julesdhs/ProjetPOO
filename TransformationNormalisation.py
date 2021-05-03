from TransformationAsbtraite import TransformationAbstraite
from TransformationCentrage import TransformationCentrage

# on définit le tableau centré réduit comme la classe fille de la classe pour les tableaux centrés

class TransformationNormalisation(TransformationCentrage):
    ''' on définit le tableau centré réduit comme la classe fille de la classe pour les tableaux centrés '''

      def transform(table):
          TransformationCentrage.transform()
          for i in range(len(table.colonnes)):
              var = variance(table,table.colonnes(i))
              if var =! 0:
                for l in table.contenu :
                  l[i]= l[i]/var







