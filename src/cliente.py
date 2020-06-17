from src.validation_utils import eh_nulo_ou_vazio, valida_email, valida_CPF


class Cliente:

    def __init__(self, email: str, CPF: str, endereco: str,
                 complemento: str, cidade: str,
                 estado: str):
        self.set_email(email)
        self.set_CPF(CPF)
        self.set_endereco(endereco)
        self.set_complemento(complemento)
        self.set_cidade(cidade)
        self.set_estado(estado)

    def set_email(self, email: str) -> None:

        if not valida_email(email):
            raise Exception("Email invalido")

        self.email = email

    def set_CPF(self, CPF: str) -> None:

        if not valida_CPF(CPF):
            raise Exception("CPF invalido")

        self.CPF = CPF

    def set_endereco(self, endereco: str) -> None:

        if eh_nulo_ou_vazio(endereco):
            raise Exception("Endereco invalido")

        self.endereco = endereco

    def set_complemento(self, complemento: str) -> None:

        if eh_nulo_ou_vazio(complemento):
            raise Exception("Complemento invalido")

        self.complemento = complemento

    def set_cidade(self, cidade: str) -> None:

        if eh_nulo_ou_vazio(cidade):
            raise Exception("Cidade invalido")

        self.cidade = cidade

    def set_estado(self, estado: str) -> None:

        if eh_nulo_ou_vazio(estado):
            raise Exception("Estado invalido")

        self.estado = estado
