#from Table import Table
from abc import ABC, abstractmethod

class OperationAbstraite(ABC):
    @abstractmethod
    def process(table):
        pass

#testé 05/05 14h