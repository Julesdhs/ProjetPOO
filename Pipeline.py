# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:52:10 2021

@author: id1846
"""
from OperationAbstraite import OperationAbstraite

class Pipeline():
    def __init__(self,process=[]) :
        self.process = process
    
    def ajout_etape(self,table,operation):
        self.process.append((table,operation))
    
    def applique(self):
        for 