from src.livro import Livro

class ColecaoDeLivro:
    def __init__(self):
        self.__lista = []
        
    def incluir(self, livro: Livro):
        if livro in self.__lista:
            raise Exception("Livro com mesmo titulo ja existe")
        self.__lista.append(livro)
    
    @property
    def lista(self):
        return self.__lista.copy()
