from abc import ABC, abstractmethod
from OperationAbstraite import OperationAbstraite

class TransformationAbstraite(OperationAbstraite,ABC):

      @abstractmethod
      def transform(self,table):
          pass
      
      def process(self,table):
         return(self.transform(table))
