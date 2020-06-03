from src.livro import Livro

from typing import Dict, Tuple


lista_livros = Dict[str, Tuple[int, float]]


class Carrinho:
    def __init__(self):
        self.__lista: lista_livros = {}
        self.__total: float = 0.0

    def addLivro(self, livro: Livro) -> None:

        if not isinstance(livro, Livro):
            raise Exception("Nao eh objeto da classe Livro")

        quant_livro = self.__lista.get(livro.get_titulo(), (0, 0.0))[0]
        #                           tupla (quantidade de livro, preço do livro)
        self.__lista[livro.get_titulo()] = (quant_livro + 1, livro.get_preco())

        self.__total += livro.get_preco()

    @property
    def lista(self) -> lista_livros:
        return self.__lista.copy()

    @property
    def total(self) -> float:
        return self.__total
