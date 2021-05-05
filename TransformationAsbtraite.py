#from Table import Table
from abc import ABC, abstractmethod

class TransformationAbstraite(OperationAbstraite):

      @abstractmethod
      def process(table):
          transform(table)
          return(table)

      @abstractmethod
      def transform(table):
          pass

#testé 05/05 14h