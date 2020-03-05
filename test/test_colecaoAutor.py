from src.autor import *
from src.colecaoAutor import *
import pytest

class TestColecaoAutor:

    @pytest.fixture
    def usuarios(self):
        autor1 = Autor('Igor','igor.nascimento@caelum.com.br','Estudante de Python e ML')
        autor2 = Autor('Thiago','thiago@hotmail.com','Estudante de Java')
        autor3 = Autor('Cassio','cassio@yahoo.org','Estudante de JavaScript')
        return autor1, autor2, autor3

    def test_quando_CriarMultiplosAutoresDeEmailsDiferentes_retorna_SalvoComSucesso(self, usuarios):
        colecao_de_autores = ColecaoDeAutores()
        colecao_de_autores.incluir(usuarios[0])
        colecao_de_autores.incluir(usuarios[1])
        colecao_de_autores.incluir(usuarios[2])
        assert colecao_de_autores.num_de_autores == 3
    
    def test_quando_CriarMultiplosAutoresIguais_retorna_Erro(self):
        autor1 = Autor('Igor Nascimento','igor.nascimento@caelum.com.br','Estudante de ML')
        autor2 = autor1
        
        colecao_de_autores = ColecaoDeAutores()
        colecao_de_autores.incluir(autor1)

        with pytest.raises(Exception):
            colecao_de_autores.incluir(autor2)

    def test_quando_CriarMultiplosAutoresDeNomesDiferentesEDeEmailsIguais_retorna_Erro(self):
        autor1 = Autor('Igor Nascimento','igor.nascimento@caelum.com.br','Estudante de ML')
        autor2 = Autor('Igor Alves','igor.nascimento@caelum.com.br','Estudante de ML')

        colecao_de_autores = ColecaoDeAutores()

        colecao_de_autores.incluir(autor1)
        with pytest.raises(Exception):
            colecao_de_autores.incluir(autor2)

    def test_quando_CriarMultiplosAutoresDeNomesIguaisEDeEmailsDiferentes_retorna_Erro(self):
        colecao_de_autores = ColecaoDeAutores()
        colecao_de_autores.incluir(Autor('Igor','igor.nascimento@caelum.com.br','Estudante de ML'))
        colecao_de_autores.incluir(Autor('Igor','igor.alves@caelum.com.br','Estudante de Python'))
        assert colecao_de_autores.num_de_autores == 2