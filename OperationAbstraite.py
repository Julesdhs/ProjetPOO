from abc import ABC, abstractmethod

class OperationAbstraite(ABC):
    @abstractmethod
    def process(self,table):
        pass

