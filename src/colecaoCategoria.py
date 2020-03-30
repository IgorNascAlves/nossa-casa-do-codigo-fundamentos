from src.categoria import Categoria
class ColecaoDeCategorias:

    def __init__(self):
        self.__lista = []

    def incluir(self,categoria: Categoria):
        if categoria in self.__lista:
            raise Exception("Categoria com nome {} já exite na Coleção".format())    
        self.__lista.append(categoria)
        
    @property
    def lista_de_autores(self):
        return self.__lista[:]