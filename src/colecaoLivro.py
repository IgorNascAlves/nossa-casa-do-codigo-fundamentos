from typing import List

from src.livro import Livro


class ColecaoDeLivro:
    def __init__(self):
        self.__lista: List[Livro] = []

    def incluir(self, livro: Livro) -> None:
        if livro in self.__lista:
            raise Exception("Colecao de livro já contem um" +
                            "livro com mesmo titulo ou isbn")
        self.__lista.append(livro)

    @property
    def lista(self):
        return self.__lista.copy()
