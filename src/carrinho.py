from src.livro import Livro

from collections import defaultdict
from typing import Dict


lista_livros = Dict[Livro, int]


class Carrinho:
    def __init__(self):

        self.__lista: lista_livros = defaultdict(int)
        self.__total: float = 0.0

    def addLivro(self, livro: Livro) -> None:

        if not isinstance(livro, Livro):
            raise Exception("Nao eh objeto da classe Livro")

        self.__lista[livro] = self.__lista[livro] + 1

        self.__total += livro.get_preco()

    @property
    def lista(self) -> lista_livros:
        return self.__lista.copy()

    @property
    def total(self) -> float:
        return self.__total
