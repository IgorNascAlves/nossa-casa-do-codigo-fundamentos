from src.autor import Autor


class ColecaoDeAutores:

    def __init__(self):
        self.__lista = []

    def incluir(self, autor: Autor):
        if autor in self.__lista:
            raise Exception("Autor com mesmo email")
        self.__lista.append(autor)

    @property
    def lista_de_autores(self):
        return self.__lista[:]
