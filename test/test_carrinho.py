from src.livro import Livro
from src.colecaoLivro import ColecaoDeLivro
from src.carrinho import Carrinho
from src.cupons import Cupons

from datetime import datetime
import pytest


class TestCarrinho:

    @pytest.fixture
    def cupons(self):
        cupons = Cupons()
        cupons.cadastra_cupom("Jovem Nerd",
                              datetime.today().date().strftime('%d/%m/%Y'))
        cupons.cadastra_cupom("Nerd Tech", "11/06/2020")
        return cupons

    @pytest.fixture
    def email(self):
        email = 'igor.nascimento@caelum.com.br'
        return email

    @pytest.fixture
    def CPF(self):
        CPF = '86297171068'
        return CPF

    @pytest.fixture
    def endereco(self):
        endereco = 'Rua Alexandre Galantai n839 Bairro Dos Casa'
        return endereco

    @pytest.fixture
    def complemento(self):
        complemento = 'casa'
        return complemento

    @pytest.fixture
    def cidade(self):
        cidade = 'São Bernardo do Campo'
        return cidade

    @pytest.fixture
    def estado(self):
        estado = 'SP'
        return estado

    @pytest.fixture
    def colecao_de_livro(self):
        colecao_de_livro = ColecaoDeLivro()
        hoje_em_string = datetime.today().date().strftime('%d/%m/%Y')

        livro1 = Livro("Machine Learning em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       30.20, 150, '978-3-16-148410-0',
                       hoje_em_string, 'Machine Learning')
        livro2 = Livro("Data Science em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       29.80, 150, '123-3-16-148410-0',
                       hoje_em_string, 'Data Science')
        livro3 = Livro("Mobile em COBOL",
                       'M'*500, '<br> **** \n <html>'*50,
                       55.20, 150, '456-3-16-148410-0',
                       hoje_em_string, 'Mobile')

        colecao_de_livro.incluir(livro1)
        colecao_de_livro.incluir(livro2)
        colecao_de_livro.incluir(livro3)

        return colecao_de_livro

    def test_qdo_AddLivroCarrinho_LivroNalista(self, cupons,
                                               colecao_de_livro
                                               ):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)

        assert livro_retornado in carrinho.lista.keys()

    def test_qdo_ListaLivroCarrinho_ListaLivrosAumenta(self, cupons,
                                                       colecao_de_livro
                                                       ):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)
        num_livros_adcionados = 1

        lista = carrinho.lista
        tamanho_lista = len(lista)

        assert num_livros_adcionados == tamanho_lista

    def test_qdo_TotalCarrinho_RetornaTotalEsperado(self, cupons,
                                                    colecao_de_livro
                                                    ):
        carrinho = Carrinho(cupons)

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

    def test_qdo_AddLivroCarrinhoTitulo_DisparaException(self, cupons,
                                                         colecao_de_livro
                                                         ):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        with pytest.raises(Exception):
            carrinho.addLivro(titulo)

    def test_qdo_AddMesmoLivroMultiplas_QuantidaAumenta(self, cupons,
                                                        colecao_de_livro
                                                        ):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)
        carrinho.addLivro(livro_retornado)
        carrinho.addLivro(livro_retornado)

        qtd_items_carrinho = len(carrinho.lista)

        assert qtd_items_carrinho == 1

    def test_qdo_AddMesmoLivroMultiplas_TotalAumenta(self, cupons,
                                                     colecao_de_livro
                                                     ):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        total_livros = livro_retornado.get_preco() * 3

        carrinho.addLivro(livro_retornado)
        carrinho.addLivro(livro_retornado)
        carrinho.addLivro(livro_retornado)

        assert carrinho.total == total_livros

    def test_qdo_FinalizaCompra_retornaID(self, cupons,
                                          colecao_de_livro,
                                          email, CPF,
                                          endereco,
                                          complemento,
                                          cidade,
                                          estado):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)

        cod_compra = carrinho.finaliza_compra(email=email, CPF=CPF,
                                              endereco=endereco,
                                              complemento=complemento,
                                              cidade=cidade, estado=estado
                                              )

        assert cod_compra is not None

    def test_qdo_FinalizaCompraComCupom_retornaID(self, cupons,
                                                  colecao_de_livro,
                                                  email, CPF,
                                                  endereco,
                                                  complemento,
                                                  cidade,
                                                  estado):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)

        cupom = "Jovem Nerd"

        cod_compra = carrinho.finaliza_compra(email=email, CPF=CPF,
                                              endereco=endereco,
                                              complemento=complemento,
                                              cidade=cidade, estado=estado,
                                              cupom=cupom
                                              )

        assert cod_compra is not None

    def test_qdo_FinalizaCompraCupomVencido_DisparaException(self, cupons,
                                                             colecao_de_livro,
                                                             email, CPF,
                                                             endereco,
                                                             complemento,
                                                             cidade,
                                                             estado):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)

        cupom = "Nerd Tech"

        with pytest.raises(Exception):
            carrinho.finaliza_compra(email=email, CPF=CPF,
                                     endereco=endereco,
                                     complemento=complemento,
                                     cidade=cidade, estado=estado,
                                     cupom=cupom
                                     )

    def test_qdo_FinalizaCompraCupomInvalido_DisparaException(self, cupons,
                                                              colecao_de_livro,
                                                              email, CPF,
                                                              endereco,
                                                              complemento,
                                                              cidade,
                                                              estado):
        carrinho = Carrinho(cupons)

        titulo = "Machine Learning em COBOL"

        livro_retornado = colecao_de_livro.busca_livro(titulo).pop()

        carrinho.addLivro(livro_retornado)

        cupom = "Fake cupom"

        with pytest.raises(Exception):
            carrinho.finaliza_compra(email=email, CPF=CPF,
                                     endereco=endereco,
                                     complemento=complemento,
                                     cidade=cidade, estado=estado,
                                     cupom=cupom
                                     )
