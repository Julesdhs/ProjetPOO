from abc import ABC, abstractmethod

class TransformationAbstraite(OpérationAbstraite):
      def process(self,table):
          transform(table)
          return(table)

      @asbtractmethod
      def transform(self,table):
          pass

