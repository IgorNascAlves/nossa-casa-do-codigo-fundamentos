from src.livro import Livro
from src.colecaoLivro import ColecaoDeLivro

from datetime import datetime
import pytest
# OK Título é único
# OK Isbn é único
# OK Como não vamos trabalhar com bancos de dados,
# precisamos usar alguma abstração que nos permita armazenar objetos.
# Sugiro utilizar a mesma tática trabalhada para o autor.


class TestColecaoLivro:
    @pytest.fixture
    def colecao_de_livro(self):
        return ColecaoDeLivro()

    @pytest.fixture
    def hoje_em_string(self):
        return datetime.today().date().strftime('%d/%m/%Y')

    def test_quando_CriarMultiplosLivros_NaoDisparaException(self,
                                                             colecao_de_livro,
                                                             hoje_em_string):
        livro1 = Livro("Machine Learning em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '978-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')
        livro2 = Livro("Data Science em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '123-3-16-148410-0',
                       hoje_em_string, 'Data Science')
        livro3 = Livro("Mobile em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '456-3-16-148410-0',
                       hoje_em_string, 'Mobile')

        colecao_de_livro.incluir(livro1)
        colecao_de_livro.incluir(livro2)
        colecao_de_livro.incluir(livro3)

        assert 3 == len(colecao_de_livro.lista)

    def test_quando_CriarLivrosTitulosIguais_DisparaException(self,
                                                              colecao_de_livro,
                                                              hoje_em_string):
        titulo = "Machine Learning em COBOL"

        livro1 = Livro(titulo, 'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '978-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')

        livro2 = Livro(titulo, 'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '753-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')

        colecao_de_livro.incluir(livro1)
        with pytest.raises(Exception):
            colecao_de_livro.incluir(livro2)

    def test_qdo_BuscaLivroCadastrado_RetornaLivro(self,
                                                   colecao_de_livro,
                                                   hoje_em_string):
        titulo = "Machine Learning em COBOL"

        livro1 = Livro(titulo, 'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '978-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')

        colecao_de_livro.incluir(livro1)

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        assert titulo == livro_retornado.get_titulo()

    def test_qdo_BuscaLivroNaoCadastrado_DisparaException(self,
                                                          colecao_de_livro,
                                                          hoje_em_string):

        titulo = 'Livro nenhum'

        with pytest.raises(Exception):
            colecao_de_livro.busca_livro(titulo)

    def test_qdo_BuscaTituloVazio_DisparaException(self,
                                                   colecao_de_livro,
                                                   hoje_em_string):

        titulo = ''

        with pytest.raises(Exception):
            colecao_de_livro.busca_livro(titulo)

    def test_qdo_BuscaTituloIncompleto_RetornaLivro(self, colecao_de_livro,
                                                    hoje_em_string):
        titulo = "Machine Learning em COBOL"

        livro1 = Livro(titulo, 'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '978-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')

        colecao_de_livro.incluir(livro1)

        titulo_incompleto = "Machine"
        livro_retornado = colecao_de_livro.busca_livro(titulo_incompleto).pop()

        assert titulo == livro_retornado.get_titulo()

    def test_quando_BuscaTituloIncompleto_RetornaMultLivro(self,
                                                           colecao_de_livro,
                                                           hoje_em_string):
        livro1 = Livro("Machine Learning em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '978-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')
        livro2 = Livro("Machine Learning em Go",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '123-3-16-148410-0',
                       hoje_em_string, 'Data Science')
        livro3 = Livro("Machine Learning em Python",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '456-3-16-148410-0',
                       hoje_em_string, 'Mobile')

        colecao_de_livro.incluir(livro1)
        colecao_de_livro.incluir(livro2)
        colecao_de_livro.incluir(livro3)

        titulo_incompleto = "Machine"
        livro_retornado = colecao_de_livro.busca_livro(titulo_incompleto)

        assert 3 == len(livro_retornado)
