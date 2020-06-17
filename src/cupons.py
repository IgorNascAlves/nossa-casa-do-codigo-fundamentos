from typing import Dict

from src.validation_utils import valida_se_data_futura


class Cupons:

    def __init__(self):
        self.__lista: Dict[str, str] = {}

    def cadastra_cupom(self, nome: str, validade: str) -> None:
        self.__lista[nome] = validade

    def valida_cupom(self, nome):
        data_cupom = self.__lista.get(nome, None)
        if data_cupom is None:
            raise Exception("Cupom não cadastrado")

        if not valida_se_data_futura(data_cupom):
            raise Exception("Cupom vencido")
