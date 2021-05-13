from EstimateurSomme import EstimateurSomme
from Table import Table
import unittest

class TestSomme(unittest.TestCase):
    def test_calcul(self):
        table=Table(['TestSomme'],[[1],[2],[3],[4],[5]])
        res=EstimateurSomme.somme(table,'TestSomme')
        self.assertEqual(res,15)
        table2=Table(['TestSomme'],[[1],[2],[3],[4.5]])
        res2=EstimateurSomme.somme(table2,'TestSomme')       
        self.assertNotEqual(res2,10)
unittest.main()

