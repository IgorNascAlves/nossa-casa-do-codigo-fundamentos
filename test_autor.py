from unittest import TestCase
from autor import *

class TestAutor(TestCase):

    def test_quando_AutorValido_retorna_DataRegistroNaoNula(self):        
        autor = Autor("Igor",'igor.nascimento@caelum.com.br', 400 * "I")
        self.assertIsNotNone(autor.data_registro)
    
    def test_quando_EmailNulo_retorna_Erro(self):
        with self.assertRaises(Exception):
            Autor("Igor",None, "Texto")

    def test_quando_EmailInvalido_retorna_Erro(self):
        with self.assertRaises(Exception):
            Autor("Igor",'igor.nascimento@caelum', "Texto")
    
    def test_quando_NomeNulo_retorna_Erro(self):
        with self.assertRaises(Exception):
            Autor(None,'igor.nascimento@caelum.com.br', "Texto")

    def test_quando_NomeEmBranco_retorna_Erro(self):
        with self.assertRaises(Exception):
            Autor(' ','igor.nascimento@caelum.com.br', "Texto")

    def test_quando_DescricaoNulo_retorna_Erro(self):
        with self.assertRaises(Exception):
            Autor("Igor",'igor.nascimento@caelum.com.br', None)

    def test_quando_DescricaoMaior400Car_retorna_Erro(self):
        with self.assertRaises(Exception):
            Autor("Igor",'igor.nascimento@caelum.com.br', 401 * 'I')