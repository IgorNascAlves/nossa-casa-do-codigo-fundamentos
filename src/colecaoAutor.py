from typing import List

from src.autor import Autor


class ColecaoDeAutores:

    def __init__(self):
        self.__lista: List[Autor] = []

    def incluir(self, autor: Autor) -> None:
        if autor in self.__lista:
            raise Exception("Autor com mesmo email")
        self.__lista.append(autor)

    @property
    def lista_de_autores(self) -> List[Autor]:
        return self.__lista[:]
