from abc import ABC, abstractmethod

class TransformationAbstraite(OperationAbstraite):
      def process(self,table):
          transform(table)
          return(table)

      @abstractmethod
      def transform(self,table):
          pass

