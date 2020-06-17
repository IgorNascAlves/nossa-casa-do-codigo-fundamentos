from src.livro import Livro
from src.cliente import Cliente
from src. cupons import Cupons

from collections import defaultdict
from typing import Dict


lista_livros = Dict[Livro, int]


class Carrinho:

    def __init__(self, cupons, cod_atual=0):
        self.cod_atual = cod_atual + 1
        self.__lista: lista_livros = defaultdict(int)
        self.__total: float = 0.0
        self.__cupons: Cupons = cupons

    def addLivro(self, livro: Livro) -> None:

        if not isinstance(livro, Livro):
            raise Exception("Nao eh objeto da classe Livro")

        self.__lista[livro] = self.__lista[livro] + 1

        self.__total += livro.get_preco()

    def finaliza_compra(self, email: str, CPF: str, endereco: str,
                        complemento: str, cidade: str,
                        estado: str, cupom: str = None):

        if cupom is not None:
            self.__cupons.valida_cupom(cupom)

        self.cliente = Cliente(email, CPF, endereco,
                               complemento, cidade, estado
                               )

        return self.cod_atual

    @property
    def lista(self) -> lista_livros:
        return self.__lista.copy()

    @property
    def total(self) -> float:
        return self.__total
