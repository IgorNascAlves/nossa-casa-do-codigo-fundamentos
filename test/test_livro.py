import pytest
from src.livro import Livro


class TestLivro:

    @pytest.fixture
    def colecao_de_autores(self):
        pass
        #return Livro()

    def test_quando_CriarLivro_NaoDispara_Exception(self):
        
        titulo = "Machine Learning em COBOL" #Obrigatorio
        resumo = 'M'*500 #Até 500 #Obrigatorio
        sumario = '<br> **** \n <html>'*50
        preco = 50.20 #a partir de 20 #Obrigatorio
        num_paginas = 150 #a partir de 100 #Obrigatorio
        isbn = '978-3-16-148410-0' #formato livre #obrigatorio
        data = '02/04/2020' #futuro
        categoria = 'Machine Learning' #nao nula
        
        livro = Livro(titulo, resumo, sumario,
                    preco, num_paginas, isbn, data, categoria)

    def test_quando_CriaLivroComTituloNulo_dispara_Exception(self):

        titulo = None #Obrigatorio
        resumo = 'M'*500 #Até 500 #Obrigatorio
        sumario = '<br> **** \n <html>'*50
        preco = 50.20 #a partir de 20 #Obrigatorio
        num_paginas = 150 #a partir de 100 #Obrigatorio
        isbn = '978-3-16-148410-0' #formato livre #obrigatorio
        data = '02/04/2020' #futuro
        categoria = 'Machine Learning' #nao nula
        
        with pytest.raises(Exception):                
            livro = Livro(titulo, resumo, sumario,
                        preco, num_paginas, isbn, data, categoria)
    
    def test_quando_CriaLivroComResumoNulo_dispara_Exception(self):

        titulo = "Machine Learning em COBOL" #Obrigatorio
        resumo = None #Até 500 #Obrigatorio
        sumario = '<br> **** \n <html>'*50
        preco = 50.20 #a partir de 20 #Obrigatorio
        num_paginas = 150 #a partir de 100 #Obrigatorio
        isbn = '978-3-16-148410-0' #formato livre #obrigatorio
        data = '02/04/2020' #futuro
        categoria = 'Machine Learning' #nao nula
        
        with pytest.raises(Exception):                
            livro = Livro(titulo, resumo, sumario,
                        preco, num_paginas, isbn, data, categoria)
        


    #def test_quando_CriarMultiplosAutoresDeEmailsDiferentes_NaoDisparaException(self):

        #assert 0 == 2

        #with pytest.raises(Exception):
            #pass