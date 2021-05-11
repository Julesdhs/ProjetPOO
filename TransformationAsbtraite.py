from abc import ABC, abstractmethod
from OperationAbstraite import OperationAbstraite

<<<<<<< HEAD
class TransformationAbstraite(OperationAbstraite):

      def process(self,table):
          transform(table)
          return(table)
=======
class TransformationAbstraite(OperationAbstraite,ABC):
>>>>>>> c7c8342d126054200534fabaa5ab6af27faf19f9

      @abstractmethod
      def transform(self,table):
          pass
      
      def process(self,table):
         return(self.transform(table))
