#from OperationAbstraite import OperationAbstraite
from abc import ABC, abstractmethod

class EstimateurAbstraite(ABC):

    @abstractmethod
    def fit(self,table):
        pass

    def process(self,table):
        return(self.fit(table))

#testé 05/05 14h