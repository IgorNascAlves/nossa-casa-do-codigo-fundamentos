from typing import List

from src.categoria import Categoria


class ColecaoDeCategorias:

    def __init__(self):
        self.__lista: List[Categoria] = []

    def incluir(self, categoria: Categoria):
        if categoria in self.__lista:
            msg = f"Categoria com nome {categoria.nome} já exite na Coleção"
            raise Exception(msg)
        self.__lista.append(categoria)

    @property
    def lista_de_categorias(self):
        return self.__lista[:]
