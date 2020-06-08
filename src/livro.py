from src.validation_utils import eh_nulo_ou_vazio, valida_se_data_futura


class Livro:

    def __init__(self, titulo, resumo, sumario,
                 preco, num_paginas, isbn, data,
                 categoria):
        self._set_titulo(titulo)
        self._set_resumo(resumo)
        self._set_sumario(sumario)
        self._set_preco(preco)
        self._set_num_paginas(num_paginas)
        self._set_isbn(isbn)
        self._set_data(data)
        self._set_categoria(categoria)

    def get_titulo(self) -> str:
        return self.__titulo

    def get_isbn(self) -> str:
        return self.__isbn

    def get_preco(self) -> float:
        return self.__preco

    def _set_titulo(self, titulo: str) -> None:
        if eh_nulo_ou_vazio(titulo):
            raise Exception("Titulo não pode ser Nulo")
        self.__titulo: str = titulo

    def _set_resumo(self, resumo: str) -> None:
        if eh_nulo_ou_vazio(resumo):
            raise Exception("Resumo não pode ser Nulo")
        if len(resumo) > 500:
            raise Exception('Resumo não pode ter mais de 500 caracteres')
        self.__resumo: str = resumo

    def _set_sumario(self, sumario: str) -> None:
        if eh_nulo_ou_vazio(sumario):
            raise Exception("Sumario não pode ser nulo")
        self.__sumario: str = sumario

    def _set_preco(self, preco: float) -> None:
        if eh_nulo_ou_vazio(preco):
            raise Exception("preco não pode ser Nulo")
        if preco < 20:
            raise Exception("Preço não pode ser inferior a 20 reias")
        self.__preco: float = preco

    def _set_num_paginas(self, num_paginas: int) -> None:
        if eh_nulo_ou_vazio(num_paginas):
            raise Exception("Numera de pagina não pode ser Nulo")
        if num_paginas < 100:
            raise Exception("Numero de pagina não pode ser inferior a 100")
        self.__num_paginas: int = num_paginas

    def _set_isbn(self, isbn: str) -> None:
        if eh_nulo_ou_vazio(isbn):
            raise Exception("isbn não pode ser Nulo")
        self.__isbn: str = isbn

    def _set_data(self, data: str) -> None:
        if not valida_se_data_futura(data):
            raise Exception("Data deve ser futura {}".format(data))
        self.__data: str = data

    def _set_categoria(self, categoria: str) -> None:
        if eh_nulo_ou_vazio(categoria):
            raise Exception("categoria não pode ser Nulo")
        self.__categoria = categoria

    def __eq__(self, livro):
        titulo_igual = self.__titulo == livro.get_titulo()
        isbn_igual = self.__isbn == livro.get_isbn()
        return titulo_igual or isbn_igual

    def __hash__(self):
        return hash(self.__titulo)
