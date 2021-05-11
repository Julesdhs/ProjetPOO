# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:52:10 2021

@author: id1846
"""
#from OperationAbstraite import OperationAbstraite

class Pipeline():
    def __init__(self,table,pile=[]) :
        self.pile = pile
        self.table = table

    def ajout_etape(self,operation):
        self.pile.append(operation)

    def applique(self):
        j=0
        for k in range(len(self.pile)):
            if len(self.pile) != 0 :
                self.pile[k-j].process(self.table)
                del self.pile[0]
                j+=1
        return(self.table)