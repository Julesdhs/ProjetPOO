from Table import table
from abc import ABC, abstractmethod

class OperationAbstraite(ABC):
    @abstractmethod
    def process(table):
        pass
