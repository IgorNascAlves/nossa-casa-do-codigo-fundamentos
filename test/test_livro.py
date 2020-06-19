import pytest  # type: ignore
from datetime import datetime, timedelta
from src.livro import Livro


class TestLivro:

    @pytest.fixture
    def colecao_autores(self):
        titulo = "Machine Learning em COBOL"
        resumo = 'M'*500
        sumario = '<br> **** \n <html>'*50
        preco = 50.20
        num_paginas = 150
        isbn = '978-3-16-148410-0'
        data = datetime.today().date().strftime('%d/%m/%Y')
        categoria = 'Machine Learning'

        return {'titulo': titulo, 'resumo': resumo, 'sumario': sumario,
                'preco': preco, 'num_paginas': num_paginas, 'isbn': isbn,
                'data': data, 'categoria': categoria}

    def test_qdo_CriarLivro_NaoDispara_Exception(self, colecao_autores):

        Livro(colecao_autores['titulo'], colecao_autores['resumo'],
              colecao_autores['sumario'], colecao_autores['preco'],
              colecao_autores['num_paginas'], colecao_autores['isbn'],
              colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriarLivroSumarioNulo_dispara_Exception(self,
                                                         colecao_autores):
        sumario = None  # Obrigatorio

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  sumario, colecao_autores['preco'],
                  colecao_autores['num_paginas'], colecao_autores['isbn'],
                  colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroTituloNulo_dispara_Exception(self, colecao_autores):

        titulo = None  # Obrigatorio

        with pytest.raises(Exception):
            Livro(titulo, colecao_autores['resumo'],
                  colecao_autores['sumario'], colecao_autores['preco'],
                  colecao_autores['num_paginas'], colecao_autores['isbn'],
                  colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroResumoNulo_dispara_Exception(self, colecao_autores):

        resumo = None  # Obrigatorio

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], resumo,
                  colecao_autores['sumario'], colecao_autores['preco'],
                  colecao_autores['num_paginas'], colecao_autores['isbn'],
                  colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroResumoMais500Chars_dispara_Exception(
                                                               self,
                                                               colecao_autores
                                                               ):

        resumo = 'M' * 501  # Até 500

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], resumo,
                  colecao_autores['sumario'], colecao_autores['preco'],
                  colecao_autores['num_paginas'], colecao_autores['isbn'],
                  colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroPrecoNulo_dispara_Exception(self, colecao_autores):

        preco = None  # Obrigatorio

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  colecao_autores['sumario'], preco,
                  colecao_autores['num_paginas'],
                  colecao_autores['isbn'], colecao_autores['data'],
                  colecao_autores['categoria'])

    def test_qdo_CriaLivroPreenorQue20_dispara_Exception(
                                                         self,
                                                         colecao_autores
                                                         ):

        preco = 19.99  # a partir de 20

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  colecao_autores['sumario'], preco,
                  colecao_autores['num_paginas'],
                  colecao_autores['isbn'], colecao_autores['data'],
                  colecao_autores['categoria'])

    def test_qdo_CriaLivroNumDePaginasNulo_dispara_Exception(
                                                             self,
                                                             colecao_autores
                                                             ):

        num_paginas = None  # Obrigatorio

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  colecao_autores['sumario'], colecao_autores['preco'],
                  num_paginas, colecao_autores['isbn'],
                  colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroNumDePagMenorQue100_dispara_Exception(
                                                                self,
                                                                colecao_autores
                                                                ):

        num_paginas = 99  # a partir de 100

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  colecao_autores['sumario'], colecao_autores['preco'],
                  num_paginas, colecao_autores['isbn'],
                  colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroIsbnNulo_dispara_Exception(self, colecao_autores):

        isbn = None  # obrigatorio

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  colecao_autores['sumario'], colecao_autores['preco'],
                  colecao_autores['num_paginas'], isbn,
                  colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroIsbnFormatado_NaoDispara_Exception(
                                                             self,
                                                             colecao_autores
                                                             ):

        isbn = '978-3-16-148410-0'  # formato livre

        Livro(colecao_autores['titulo'], colecao_autores['resumo'],
              colecao_autores['sumario'], colecao_autores['preco'],
              colecao_autores['num_paginas'], isbn,
              colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroIsbnNaoFormatado_NaoDispara_Exception(
                                                                self,
                                                                colecao_autores
                                                                ):

        isbn = '9783161484100'  # formato livre

        Livro(colecao_autores['titulo'], colecao_autores['resumo'],
              colecao_autores['sumario'], colecao_autores['preco'],
              colecao_autores['num_paginas'], isbn,
              colecao_autores['data'], colecao_autores['categoria'])

    def test_qdo_CriaLivroDataMenorDataAtual_dispara_Exception(
                                                               self,
                                                               colecao_autores
                                                               ):
        hoje = datetime.today().date()
        ontem = hoje - timedelta(days=1)
        data = ontem.strftime('%d/%m/%Y')  # data futuro

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  colecao_autores['sumario'], colecao_autores['preco'],
                  colecao_autores['num_paginas'],
                  colecao_autores['isbn'], data,
                  colecao_autores['categoria'])

    def test_qdo_CriaLivroCategoriaNulo_dispara_Exception(
                                                             self,
                                                             colecao_autores
                                                             ):

        categoria = None  # nao nula

        with pytest.raises(Exception):
            Livro(colecao_autores['titulo'], colecao_autores['resumo'],
                  colecao_autores['sumario'], colecao_autores['preco'],
                  colecao_autores['num_paginas'],
                  colecao_autores['isbn'], colecao_autores['data'],
                  categoria
                  )
