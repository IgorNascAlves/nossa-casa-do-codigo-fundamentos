from typing import List

from src.livro import Livro
from src.validation_utils import eh_nulo_ou_vazio


class ColecaoDeLivro:
    def __init__(self):
        self.__lista: List[Livro] = []

    def incluir(self, livro: Livro) -> None:
        if livro in self.__lista:
            raise Exception("Colecao de livro já contem um" +
                            "livro com mesmo titulo ou isbn")
        self.__lista.append(livro)

    @property
    def lista(self):
        return self.__lista.copy()

    def busca_livro(self, titulo: str) -> List[Livro]:
        resultado: List[Livro] = []
        if eh_nulo_ou_vazio(titulo):
            raise Exception(f"Titulo não pode ser nulo ou vazio")

        for livro in self.lista:
            if titulo in livro.get_titulo():
                resultado.append(livro)
        if len(resultado) == 0:
            raise Exception(f"Livro com o titulo {titulo} não encontrado")
        return resultado
