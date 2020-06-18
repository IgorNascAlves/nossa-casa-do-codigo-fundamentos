from typing import List

from src.validation_utils import valida_se_data_futura
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
        else:
            data_cupom = self.__lista[ind].get_validade()
        if not valida_se_data_futura(data_cupom):
            raise Exception("Cupom vencido")
