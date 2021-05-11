import csv as csv

class Table(object) :

    def __init__(self, colonnes=None, contenu=None):
        if contenu is None:
            contenu = [[]]
        if colonnes is None:
            colonnes = []
        self.colonnes = colonnes
        self.contenu = contenu

    def ajoutcol(self,nomcol,col,pos=99999):
        """
        /!\ position est ici utilisé comme "premier" ou "deuxième" en partant du début (indice dans la liste +1)
        la colonne doit avoir la bonne dimension
        pos est par défaut un entier grand arbitraire pour ajouter la colonne au bout par défaut"""
        self.colonnes = self.colonnes[:pos-1]+[nomcol]+self.colonnes[pos-1:]
        if len(col) != len(self.contenu):
            print('pas la même taille')

        if len(col) == len(self.contenu):
            for k in range(len(col)):
                self.contenu[k] = self.contenu[k][:pos-1]+[col[k]]+self.contenu[k][pos-1:]

    def enlevcol(self,pos=-1):
        """
        par défaut on enlève la 1ère
        """
        if pos != -1 :
            self.colonnes = self.colonnes[:pos-1] + self.colonnes[pos:]
            for k in range(len(self.contenu)):
                self.contenu[k] = self.contenu[k][:pos-1]+self.contenu[k][pos:]
        if pos == -1 :
            self.colonnes = self.colonnes[:pos]
            for k in range(len(self.contenu)):
                self.contenu[k] = self.contenu[k][:pos]


    def ajoutlig(self,ligne,pos=-1):
        if pos != -1 :
            self.contenu = self.contenu[:pos]+[ligne]+self.contenu[pos:]
        if pos == -1 :
            self.contenu = self.contenu[:99999]+[ligne]

    def enlevlig(self,pos=-1):
        if pos != -1 :
            self.contenu = self.contenu[:pos-1]+self.contenu[pos:]
        if pos == -1 :
            self.contenu = self.contenu[:pos]

    def export(self,nom):

        with open(nom, 'w') as f:

            write = csv.writer(f, delimiter = ',')
            write.writerow(self.colonnes)
            write.writerows(self.contenu)

    def stringtoint(self,nomvar):
        ind = self.colonnes.index(nomvar)
        n = len(self.contenu)
        for i in range(n):
            self.contenu[i][ind]=int(self.contenu[i][ind])

#testé 05/05 14h
