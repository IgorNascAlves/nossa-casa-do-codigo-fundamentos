from typing import List

from src.categoria import Categoria


class ColecaoDeCategorias:

    def __init__(self):
        self.__lista: List[Categoria] = []

    def incluir(self, categoria: Categoria) -> None:
        if categoria in self.__lista:
            raise Exception("Categoria com nome {} já exite na Coleção".format(
                categoria.nome))
        self.__lista.append(categoria)

    @property
    def lista_de_categorias(self) -> List[Categoria]:
        return self.__lista[:]
