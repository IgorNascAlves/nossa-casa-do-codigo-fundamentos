from datetime import date
import re

from src.validation_utils import eh_nulo_ou_vazio


class Autor:

    def __init__(self, nome, email, descricao):
        self.__set_nome(nome)
        self.__set_email(email)
        self.__set_descricao(descricao)
        self.__data_registro: date = date.today()

    def __set_nome(self, nome):

        # Verifica se nome eh nulo, vazio ou em branco
        if eh_nulo_ou_vazio(nome):
            raise Exception("Nome nulo")

        self.__nome: str = nome

    def __set_email(self, email):

        regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

        # verifica se email eh valido
        if not re.search(regex, email):
            raise Exception("Email errado")
        self.__email: str = email

        self.__email = email

    def __set_descricao(self, descricao):

        # verifica se descricao esta em branco
        if eh_nulo_ou_vazio(descricao):
            raise Exception("Descricao Nula")

        # verifica se descricao tem mais de 400 caracteres
        if len(descricao) > 400:
            raise Exception("Descricao com mais de 400 car")

        self.__descricao: str = descricao

    @property
    def data_registro(self) -> date:
        return self.__data_registro

    @property
    def email(self) -> str:
        return self.__email

    def __str__(self):
        # imprime classe formatada
        string = f'Nome: {self.__nome}\n'
        string += f'Email: {self.__email}\n'
        string += f'Descricao: {self.__descricao}\n'
        string += f'Data: {self.data_registro}\n'
        return string

    def __eq__(self, autor):
        return self.email == autor.email
