class Pipeline():
    def __init__(self):
        self.operations=[]

    def ajoute_etape(self,etape):
        self.operations.append(etape)
        
    def run(self,table):
        for etape in self.operations:
            table=etape.process(table)
        return(table)
