from datetime import date
import re
class Autor:
    
    def __init__(self, nome, email, descricao):
        self.nome = nome
        self.email = email
        self.descricao = descricao
        self.__data_registro = date.today()

    @property
    def nome(self):
        return self.__nome

    @nome.setter     
    def nome(self, nome):
        #Verifica se nome eh nulo, vazio ou em branco
        if nome not in (None, '', ' '):
            self.__nome = nome
        else:
            raise Exception("Nome nulo")

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        #verifica se email eh valido
        if re.search(regex,email):
            self.__email = email
        else:
            raise Exception("Email errado")
    
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        #verifica se descricao esta em branco
        if not descricao :
            raise Exception("Descricao Nula")
        #verifica se descricao tem mais de 400 caracteres
        elif len(descricao) > 400:
            raise Exception("Descricao com mais de 400 car")
        else:
            self.__descricao = descricao

    @property
    def data_registro(self):
        #formata data para padrao brasileiro
        return f"{self.__data_registro.day}/{self.__data_registro.month}/{self.__data_registro.year}"
    
    def __str__(self):
        #imprime classe formatada
        return f'Nome: {self.nome}\nEmail: {self.email}\nDescricao: {self.descricao}\nData: {self.data_registro}\n'