from src.autor import Autor
from src.colecaoAutor import ColecaoDeAutores
import pytest


class TestColecaoAutor:

    @pytest.fixture
    def colecao_de_autores(self):
        return ColecaoDeAutores()

    def test_quando_CriarMultiplosAutoresDeEmailsIguais_dispara_Exception(
                                                 self, colecao_de_autores):
        email = 'igor.nascimento@caelum.com.br'

        autor1 = Autor('Igor Nascimento', email, 'Estudante de ML')
        autor2 = Autor('Igor Alves', email, 'Estudante de Python')

        colecao_de_autores.incluir(autor1)

        with pytest.raises(Exception):
            colecao_de_autores.incluir(autor2)

    def test_quando_CriarMultiplosAutoresDeEmailsDiferentes_SemException(
                                                self, colecao_de_autores):
        autor1 = Autor('Igor', 'igor.nascimento@caelum.com.br',
                       'Estudante de ML')
        autor2 = Autor('Igor', 'igor.alves@caelum.com.br',
                       'Estudante de Python')

        colecao_de_autores.incluir(autor1)
        colecao_de_autores.incluir(autor2)

        assert len(colecao_de_autores.lista_de_autores) == 2

    def test_quando_AcessaListaDaColecaoDeAutores_retorna_ListaDosAutores(
                                                 self, colecao_de_autores):
        lista_autores_entrada = []

        lista_autores_entrada.append(
            Autor('Igor', 'igor.nascimento@caelum.com.br',
                  'Estudante de Python e ML'))
        lista_autores_entrada.append(
            Autor('Thiago', 'thiago@hotmail.com', 'Estudante de Java'))
        lista_autores_entrada.append(
            Autor('Cassio', 'cassio@yahoo.org', 'Estudante de JavaScript'))

        for item in lista_autores_entrada:
            colecao_de_autores.incluir(item)

        assert lista_autores_entrada == colecao_de_autores.lista_de_autores
