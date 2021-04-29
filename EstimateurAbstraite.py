from Table import Table
from abc import ABC, abstractmethod

class EstimateurAbstraite(ABC):
    def process(table):
        fit(table)
    
    @abstractmethod
    def fit(table):
        pass
