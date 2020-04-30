from src.validation_utils import eh_nulo_ou_vazio


class Categoria:
    def __init__(self, nome):
        self.__set_nome(nome)

    @property
    def nome(self):
        return self.__nome

    def __set_nome(self, nome):
        if eh_nulo_ou_vazio(nome):
            raise Exception("Nome nulo")
        self.__nome = nome

    def __eq__(self, categoria):
        return self.__nome == categoria.__nome
