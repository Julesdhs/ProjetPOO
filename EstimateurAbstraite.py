#from OperationAbstraite import OperationAbstraite
#from abc import ABC, abstractmethod

class EstimateurAbstraite(OperationAbstraite, ABC):

    @abstractmethod
    def fit(self,table):
        pass

    def process(self,table):
        return(self.fit(table))

