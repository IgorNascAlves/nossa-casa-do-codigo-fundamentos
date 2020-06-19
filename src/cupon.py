from src.validation_utils import eh_nulo_ou_vazio, valida_se_data_futura


class Cupon:
    def __init__(self, nome: str, validade: str, desconto: int):
        self.set_nome(nome)
        self.set_validade(validade)
        self.set_desconto(desconto)

    def set_nome(self, nome: str) -> None:
        if eh_nulo_ou_vazio(nome):
            raise Exception("Cupon deve ter nome valido")
        self.__nome = nome

    def set_desconto(self, desconto: int) -> None:
        if eh_nulo_ou_vazio(desconto):
            raise Exception("Cupon deve ter desconto valido")
        self.__desconto = desconto

    def set_validade(self, validade: str) -> None:
        self.__validade = validade

    def get_validade(self) -> str:
        return self.__validade

    def __eq__(self, nome):
        return self.__nome == nome

    def eh_valido(self) -> bool:
        return valida_se_data_futura(self.__validade)
