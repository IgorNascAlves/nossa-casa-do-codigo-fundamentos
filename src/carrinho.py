from src.livro import Livro

from typing import List


class Carrinho:
    def __init__(self):
        self.__lista = []
        self.__total = 0.0

    def addLivro(self, livro: Livro) -> None:
        if not isinstance(livro, Livro):
            raise Exception("Nao eh objeto da classe Livro")
        self.__lista.append(livro)
        self.__total += livro.get_preco()

    @property
    def lista(self) -> List[Livro]:
        return self.__lista[:]

    @property
    def total(self) -> float:
        return self.__total
