from unittest import TestCase
from src.categoria import Categoria
from src.colecaoCategoria import ColecaoDeCategorias


class TestColecaoCategoria(TestCase):

    def test_quando_CriaMultiplasCategoria_retorna_SemErro(self):
        categoria1 = Categoria("Machine Learning")
        categoria2 = Categoria("Data Science")
        categoria3 = Categoria("Python")
        colecao_categorias = ColecaoDeCategorias()
        colecao_categorias.incluir(categoria1)
        colecao_categorias.incluir(categoria2)
        colecao_categorias.incluir(categoria3)
        self.assertEqual(3, len(colecao_categorias.lista_de_categorias))

    def test_quando_CriaCategoriasComMesmoNome_retorna_Erro(self):
        categoria1 = Categoria("Machine Learning")
        categoria2 = Categoria("Machine Learning")
        colecao_categorias = ColecaoDeCategorias()
        colecao_categorias.incluir(categoria1)
        with self.assertRaises(Exception):
            colecao_categorias.incluir(categoria2)
