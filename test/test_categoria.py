from unittest import TestCase
from src.categoria import Categoria

class TestCategoria(TestCase):

    def test_quando_CriaCategoria_retorna_SemErro(self):
        autor = Categoria("Machine Learning")
        self.assertIsNotNone(str(autor))
    
    def test_quando_DescricaoVazia_retorna_Erro(self):
        with self.assertRaises(Exception):
            Categoria(" ")
    def test_quando_DescricaoVazia_retorna_Erro(self):
        with self.assertRaises(Exception):
            Categoria(None)