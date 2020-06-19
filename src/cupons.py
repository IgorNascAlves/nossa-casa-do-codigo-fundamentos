from typing import List

from src.cupon import Cupon


class Cupons:

    def __init__(self):
        self.__lista: List[Cupon] = []

    def cadastra_cupom(self, cupon: Cupon) -> None:
        self.__lista.append(cupon)

    def valida_cupom(self, nome):
        try:
            ind = self.__lista.index(nome)
        except ValueError:
            raise Exception("Cupom não cadastrado")
        if not self.__lista[ind].eh_valido():
            raise Exception("Cupom vencido")
