
#from OperationAbstraite import OperationAbstraite

class Pipeline():
    def __init__(self,table,pile = None,res = None) :
        self.table = table
        if pile is None:
            pile = []
        if res is None :
            res = []
        self.pile = pile
        self.res = res

    def ajout_etape(self,operation):
        self.pile.append(operation)

    def applique(self):
        for k in range(len(self.pile)):
                self.res.append(self.pile[k].process(self.table))
<<<<<<< HEAD
        return(self.res)
=======
        return(self.res)
>>>>>>> 0d2d1423aafeb89090a708e0f7977664b2862d0c
