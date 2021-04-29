from abc import ABC, abstractmethod
from EstimateurAbstraite import EstimateurAbstraite

class OperationAbstraite(ABC):
    @abstractmethod
    def process(table):
        pass
