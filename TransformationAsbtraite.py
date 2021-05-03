from Table import Table
from abc import ABC, abstractmethod

class TransformationAbstraite(OpérationAbstraite):
      @abstractmethod
      def process(table):
          transform(table)
          return(table)

      @asbtractmethod
      def transform(table):
          pass

