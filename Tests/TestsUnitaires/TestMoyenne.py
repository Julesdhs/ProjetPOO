from EstimateurMoyenne import EstimateurMoyenne
from Table import Table
import unittest

class TestMoyenne(unittest.TestCase):
    def test_calcul(self):
        table=Table(['TestMoyenne'],[[1],[2],[3],[4],[5]])
        res=EstimateurMoyenne.moyenne(table,'TestMoyenne')
        self.assertEqual(res,3.0)
        table2=Table(['TestMoyenne'],[[1],[2],[3],[4.5]])
        res2=EstimateurMoyenne.moyenne(table2,'TestMoyenne')       
        self.assertNotEqual(res2,10)
unittest.main()

