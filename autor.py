from datetime import date
import re

class Autor:
    
    def __init__(self, nome, email, descricao):
        self.__set_nome(nome)
        self.__set_email(email)
        self.__set_descricao(descricao)
        self.__data_registro = date.today()

    def __set_nome(self, nome):
        
        #Verifica se nome eh nulo, vazio ou em branco
        if nome in (None, '', ' '):
            raise Exception("Nome nulo")

        self.__nome = nome

    def __set_email(self, email):
        
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        
        #verifica se email eh valido
        if not re.search(regex,email):
            raise Exception("Email errado")

        self.__email = email
    
    def __set_descricao(self, descricao):

        #verifica se descricao esta em branco
        if not descricao :
            raise Exception("Descricao Nula")

        #verifica se descricao tem mais de 400 caracteres
        if len(descricao) > 400:
            raise Exception("Descricao com mais de 400 car")

        self.__descricao = descricao

    @property
    def data_registro(self):
        return self.__data_registro
    
    def __str__(self):
        #imprime classe formatada
        return f'Nome: {self.__nome}\nEmail: {self.__email}\nDescricao: {self.__descricao}\nData: {self.data_registro}\n'