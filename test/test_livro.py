import pytest
from datetime import datetime, timedelta
from src.livro import Livro


class TestLivro:

    @pytest.fixture
    def colecao_de_autores(self):
        titulo = "Machine Learning em COBOL"
        resumo = 'M'*500 
        sumario = '<br> **** \n <html>'*50
        preco = 50.20 
        num_paginas = 150 
        isbn = '978-3-16-148410-0'
        data = datetime.today().date().strftime('%d/%m/%Y')
        categoria = 'Machine Learning'

        return {'titulo' : titulo, 'resumo' : resumo, 'sumario' : sumario,
         'preco' : preco, 'num_paginas' : num_paginas, 'isbn' : isbn, 'data' : data,
          'categoria' : categoria}

    def test_quando_CriarLivro_NaoDispara_Exception(self, colecao_de_autores):
        
        livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
        colecao_de_autores['sumario'], colecao_de_autores['preco'], colecao_de_autores['num_paginas'],
        colecao_de_autores['isbn'], colecao_de_autores['data'], colecao_de_autores['categoria'])

    def test_quando_CriaLivroComTituloNulo_dispara_Exception(self, colecao_de_autores):

        titulo = None #Obrigatorio
        
        with pytest.raises(Exception):                
            livro = Livro(titulo, colecao_de_autores['resumo'], colecao_de_autores['sumario'],
             colecao_de_autores['preco'], colecao_de_autores['num_paginas'],
                        colecao_de_autores['isbn'], colecao_de_autores['data'],
                         colecao_de_autores['categoria'])
    
    def test_quando_CriaLivroComResumoNulo_dispara_Exception(self, colecao_de_autores):

        resumo = None #Obrigatorio
        
        with pytest.raises(Exception):                
            livro = Livro(colecao_de_autores['titulo'], resumo,
            colecao_de_autores['sumario'], colecao_de_autores['preco'], colecao_de_autores['num_paginas'],
            colecao_de_autores['isbn'], colecao_de_autores['data'], colecao_de_autores['categoria'])
    
    def test_quando_CriaLivroComResumoComMaisDe500Chars_dispara_Exception(self, colecao_de_autores):

        resumo = 'M' * 501 #Até 500
        
        with pytest.raises(Exception):                
            livro = Livro(colecao_de_autores['titulo'], resumo,
            colecao_de_autores['sumario'], colecao_de_autores['preco'], colecao_de_autores['num_paginas'],
            colecao_de_autores['isbn'], colecao_de_autores['data'], colecao_de_autores['categoria'])
        
    def test_quando_CriaLivroComPrecoNulo_dispara_Exception(self, colecao_de_autores):

        preco = None #Obrigatorio
        
        with pytest.raises(Exception):                
            livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
                        colecao_de_autores['sumario'], preco, colecao_de_autores['num_paginas'],
                        colecao_de_autores['isbn'], colecao_de_autores['data'],
                         colecao_de_autores['categoria'])

    def test_quando_CriaLivroComPrecoMenorQue20_dispara_Exception(self, colecao_de_autores):

        preco = 19.99 #a partir de 20
        
        with pytest.raises(Exception):                
            livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
                        colecao_de_autores['sumario'], preco, colecao_de_autores['num_paginas'],
                        colecao_de_autores['isbn'], colecao_de_autores['data'],
                         colecao_de_autores['categoria'])

    def test_quando_CriaLivroComNumDePaginasNulo_dispara_Exception(self, colecao_de_autores):

        num_paginas = None #Obrigatorio
        
        with pytest.raises(Exception):                
            livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
                        colecao_de_autores['sumario'], colecao_de_autores['preco'],
                        num_paginas, colecao_de_autores['isbn'], 
                        colecao_de_autores['data'], colecao_de_autores['categoria'])

    def test_quando_CriaLivroComNumDePaginasMenorQue100_dispara_Exception(self, colecao_de_autores):

        num_paginas = 99 #a partir de 100
        
        with pytest.raises(Exception):                
            livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
                        colecao_de_autores['sumario'], colecao_de_autores['preco'],
                        num_paginas, colecao_de_autores['isbn'], 
                        colecao_de_autores['data'], colecao_de_autores['categoria'])

    def test_quando_CriaLivroComIsbnNulo_dispara_Exception(self, colecao_de_autores):
        
        isbn = None #obrigatorio

        with pytest.raises(Exception):
            livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
             colecao_de_autores['sumario'], colecao_de_autores['preco'],  colecao_de_autores['num_paginas'],
             isbn,  colecao_de_autores['data'], colecao_de_autores['categoria'])

    def test_quando_CriaLivroComIsbnFormatado_NaoDispara_Exception(self, colecao_de_autores):
        
        isbn = '978-3-16-148410-0' #formato livre

        livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
        colecao_de_autores['sumario'], colecao_de_autores['preco'],  colecao_de_autores['num_paginas'],
        isbn,  colecao_de_autores['data'], colecao_de_autores['categoria'])

    def test_quando_CriaLivroComIsbnNaoFormatado_NaoDispara_Exception(self, colecao_de_autores):
    
        isbn = '9783161484100' #formato livre

        livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
            colecao_de_autores['sumario'], colecao_de_autores['preco'],  colecao_de_autores['num_paginas'],
            isbn,  colecao_de_autores['data'], colecao_de_autores['categoria'])
    
    def test_quando_CriaLivroComDataMenorQueDataAtual_dispara_Exception(self, colecao_de_autores):
        hoje = datetime.today().date()
        ontem = hoje - timedelta(days = 1)
        data =  ontem.strftime('%d/%m/%Y')#futuro

        with pytest.raises(Exception):
            livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
                colecao_de_autores['sumario'], colecao_de_autores['preco'],  colecao_de_autores['num_paginas'],
                colecao_de_autores['isbn'], data, colecao_de_autores['categoria'])

    def test_quando_CriaLivroComCategoriaNulo_dispara_Exception(self, colecao_de_autores):
        
        categoria = None #nao nula

        with pytest.raises(Exception):
            livro = Livro(colecao_de_autores['titulo'], colecao_de_autores['resumo'],
             colecao_de_autores['sumario'], colecao_de_autores['preco'],  colecao_de_autores['num_paginas'],
             colecao_de_autores['isbn'],  colecao_de_autores['data'], categoria)
    
    #assert 0 == 2