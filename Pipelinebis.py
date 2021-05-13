class Pipeline():
    def __init__(self):
        self.operations=[]
    
    def ajout_etape(self,etape):
        self.operations.append(etape)
        
    def applique(self,table):
        res=[]
        for etape in self.operations:
            res.append(etape.process(table))
        return(res)
