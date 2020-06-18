from src.validation_utils import eh_nulo_ou_vazio


class Cupon:
    def __init__(self, nome: str, validade: str):
        self.set_nome(nome)
        self.set_validade(validade)

    def set_nome(self, nome: str) -> None:
        if eh_nulo_ou_vazio(nome):
            raise Exception("Cupon deve ter nome valido")
        self.__nome = nome

    def set_validade(self, validade: str) -> None:
        self.__validade = validade

    def get_validade(self) -> str:
        return self.__validade

    def __eq__(self, nome):
        return self.__nome == nome
