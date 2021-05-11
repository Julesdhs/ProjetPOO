#from OperationAbstraite import OperationAbstraite

class Pipeline():
    def __init__(self,table,pile= None) :
        self.table = table
        if pile is None:
            pile = []
        self.pile = pile

    def ajout_etape(self,operation):
        self.pile.append(operation)

    def applique(self):
        res=[]
        j=0
        for k in range(len(self.pile)):
            if len(self.pile) != 0 :
                res.append(self.pile[k-j].process(self.table))
                del self.pile[0]
                j+=1
        return(res)