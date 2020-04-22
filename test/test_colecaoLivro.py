from src.livro import *
from src.colecaoLivro import *
from datetime import datetime, timedelta
import pytest

# Um livro pertence a uma categoria
# Título é único
# Isbn é único
# Como não vamos trabalhar com bancos de dados,
# precisamos usar alguma abstração que nos permita armazenar objetos.
# Sugiro utilizar a mesma tática trabalhada para o autor.

class TestColecaoLivro:
    @pytest.fixture
    def colecao_de_livro(self):
        return ColecaoDeLivro()

    @pytest.fixture
    def hoje_em_string(self):
        return datetime.today().date().strftime('%d/%m/%Y')

    def test_quando_CriarMultiplosLivros_NaoDisparaException(self, colecao_de_livro, hoje_em_string):
        livro1 =  Livro("Machine Learning em COBOL", 'M'*500, '<br> **** \n <html>'*50,
        50.20, 150, '978-3-16-148410-0', hoje_em_string, 'Machine Learning')
        livro2 =  Livro("Data Science em COBOL", 'M'*500, '<br> **** \n <html>'*50,
        50.20, 150, '123-3-16-148410-0', hoje_em_string, 'Data Science')
        livro3 =  Livro("Mobile em COBOL", 'M'*500, '<br> **** \n <html>'*50,
        50.20, 150, '456-3-16-148410-0', hoje_em_string, 'Mobile')
        
        colecao_de_livro.incluir(livro1)
        colecao_de_livro.incluir(livro2)
        colecao_de_livro.incluir(livro3)

        assert 3 == len(colecao_de_livro.lista)

    def test_quando_CriarLivrosComTitulosIguais_DisparaException(self, colecao_de_livro, hoje_em_string):
        titulo = "Machine Learning em COBOL"
        
        livro1 =  Livro(titulo, 'M'*500, '<br> **** \n <html>'*50,
        50.20, 150, '978-3-16-148410-0', hoje_em_string, 'Machine Learning')

        livro2 =  Livro(titulo, 'M'*500, '<br> **** \n <html>'*50,
        50.20, 150, '753-3-16-148410-0', hoje_em_string, 'Machine Learning')

        colecao_de_livro.incluir(livro1)
        with pytest.raises(Exception):
            colecao_de_livro.incluir(livro2)
