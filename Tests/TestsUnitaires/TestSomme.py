from EstimateurSomme import EstimateurSomme
from EstimateurMoyenne import EstimateurMoyenne
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

class TestMoyenne(unittest.TestCase):
    def test_calcul(self):
        table=Table(['TestMoyenne'],[[1],[2],[3],[4],[5]])
        res=EstimateurMoyenne.moyenne(table,'TestMoyenne')
        self.assertEqual(res,3.0)
        table2=Table(['TestMoyenne'],[[1],[2],[3],[4.5]])
        res2=EstimateurMoyenne.moyenne(table2,'TestMoyenne')       
        self.assertNotEqual(res2,10)
unittest.main()


class SelectionTest(unittest.TestCase):
    def test_choice(self):
        self.assertTrue(True)
unittest.main()