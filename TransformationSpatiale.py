from TransformationAsbtraite import TransformationAbstraite


class TransformationSpatiale(TransformationAbstraite):
      '''les données sont indexées par région ou département : les méthodes ici vont permettre de passer d'une granularité départementale à régionale ou nationale

      L'attribut correspondra à l'espace de départ et on implémentera une méthode pour l'agrégation

      L'espace de départ s'adaptera aux données du tableau considéré, si les données sont ordonnées par région alors espace_depart sera initialisé à 1 autrement il sera initialisé à 0 (département)

      L'espace final sera un entier, soit 1 ou 2 pour l'agrégation respective régionale ou nationale;

        '''
      def __init__(table,espace_depart='problemetableau'):
            if dep in table.colonnes :
                 espace_depart = 0
            if numreg or reg in table.colonnes :
                  espace_depart = 1
            self.espace_depart = espace_depart

      def transform(self,table,espace_final):

            ''' on crée un dictionnaire des régions composées de leurs départements ; les régions sont ici les numéros que l'on retrouve dans les variables numreg '''

            dic = {1:[971],2:[972],3:[973],4:[974],6:[976],11:[75,77,78,91,92,93,94,95],24:[18,28,36,37,41,45],27:[21,25,39,58,70,71,89,90],28:[14,27,50,61,76],32:[2,59,60,62,80],44:[8,10,51,52,54,55,57,67,68,88],52:[44,49,53,72,85],53:[22,29,35,56],75:[16,17,19,23,24,33,40,47,64,79,86,87],76:[9,11,12,30,31,32,34,46,48,65,66,81,82],84:[1,3,7,15,26,38,42,43,63,69,73,74], 93: [4,5,6,13,83,84],94:[2]}

        ''' premier cas : l'espace de départ possède une granularité départementale ; on va passer à une granularité régionale
           La variable jour est présente dans toutes les données, mais aussi il y a la variable sexe dans certaines '''

            if self.espace_depart == 0 :
                  if espace_final == 1:














