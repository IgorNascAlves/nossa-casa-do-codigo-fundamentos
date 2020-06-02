from src.livro import Livro
from src.colecaoLivro import ColecaoDeLivro
from src.carrinho import Carrinho

from datetime import datetime
import pytest


class TestCarrinho:

    @pytest.fixture
    def colecao_de_livro(self):
        colecao_de_livro = ColecaoDeLivro()
        hoje_em_string = datetime.today().date().strftime('%d/%m/%Y')

        livro1 = Livro("Machine Learning em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '978-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')
        livro2 = Livro("Data Science em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       29.80, 150, '123-3-16-148410-0',
                       hoje_em_string, 'Data Science')
        livro3 = Livro("Mobile em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       50.20, 150, '456-3-16-148410-0',
                       hoje_em_string, 'Mobile')

        colecao_de_livro.incluir(livro1)
        colecao_de_livro.incluir(livro2)
        colecao_de_livro.incluir(livro3)

        return colecao_de_livro

    def test_quando_AddLivroCarrinho_LivroNalista(self,
                                                  colecao_de_livro
                                                  ):
        carrinho = Carrinho()

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)

        assert titulo in carrinho.lista.keys()

    def test_quando_ListaLivroCarrinho_NaoDisparaException(self,
                                                           colecao_de_livro
                                                           ):
        carrinho = Carrinho()

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)
        num_livros_adcionados = 1

        lista = carrinho.lista
        tamanho_lista = len(lista)

        assert num_livros_adcionados == tamanho_lista

    def test_quando_TotalCarrinho_NaoDisparaException(self,
                                                      colecao_de_livro
                                                      ):
        carrinho = Carrinho()

        titulo1 = "Machine Learning em COBOL"
        titulo2 = "Data Science em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo1).pop()
        valor_livro_1 = livro_retornado.get_preco()
        carrinho.addLivro(livro_retornado)

        livro_retornado = colecao_de_livro.busca_livro(titulo2).pop()
        valor_livro_2 = livro_retornado.get_preco()
        carrinho.addLivro(livro_retornado)

        total_carrinho_real = valor_livro_1 + valor_livro_2

        total_carrinho_retorno = carrinho.total

        assert total_carrinho_real == total_carrinho_retorno

    def test_quando_AddLivroCarrinhoTitulo_DisparaException(self,
                                                            colecao_de_livro
                                                            ):
        carrinho = Carrinho()

        titulo = "Machine Learning em COBOL"

        with pytest.raises(Exception):
            carrinho.addLivro(titulo)

    def test_quando_AddMesmoLivroMultiplas_QuantidaAumenta(self,
                                                           colecao_de_livro
                                                           ):
        carrinho = Carrinho()

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)
        carrinho.addLivro(livro_retornado)

        assert carrinho.lista[titulo][0] == 2
