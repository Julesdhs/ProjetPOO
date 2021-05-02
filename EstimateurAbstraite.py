from OperationAbstraite import OperationAbstraite
from abc import ABC, abstractmethod

class EstimateurAbstraite(ABC):
   
    @abstractmethod
    def fit(self,table):
        pass

    def process(self,table):
        fit(self,table)

