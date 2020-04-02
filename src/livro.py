class Livro:
    def __init__(self, titulo, resumo, sumario,
                preco, num_paginas, isbn, data,
                categoria):
        self._set_titulo(titulo)
        self._set_resumo(resumo)
        self._sumario = sumario
        self._set_preco(preco)
        self._set_num_paginas(num_paginas)
        self._set_isbn(isbn)
        self._set_data(data)
        self._set_categoria(categoria)

    def _set_titulo(self, titulo):
        if titulo in [None, '', ' ']:
            raise Exception("Titulo não pode ser Nulo")
        self.__titulo = titulo

    def _set_resumo(self, resumo):
        if resumo in [None, '', ' ']:
            raise Exception("Resumo não pode ser Nulo")
        self.__resumo = resumo

    def _set_preco(self, preco):
        self.__preco = preco

    def _set_num_paginas(self, num_paginas):
        self.__num_paginas = num_paginas

    def _set_isbn(self, isbn):
        self.__isbn = isbn

    def _set_data(self, data):
        self.__data = data

    def _set_categoria(self, categoria):
        self.__categoria = categoria