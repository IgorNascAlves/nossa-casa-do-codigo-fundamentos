from src.autor import *
class ColecaoDeAutores:

    def __init__(self):
        self.__lista = []

    def incluir(self,autor: Autor):
        if autor in self.__lista:
            raise Exception("Autor com mesmo email")    
        self.__lista.append(autor)

    def busca_por_email(self, email):
        for item in self.lista_de_autores:
            if item.email == email:
                return item
        raise Exception("Autor não encontrado")

    @property
    def lista_de_autores(self):
        return self.__lista[:]