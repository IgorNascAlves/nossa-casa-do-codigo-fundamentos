from datetime import datetime, date
import re
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

    def _set_titulo(self, titulo):
        if titulo in [None, '', ' ']:
            raise Exception("Titulo não pode ser Nulo")
        self.__titulo = titulo

    def _set_resumo(self, resumo):
        if resumo in [None, '', ' ']:
            raise Exception("Resumo não pode ser Nulo")
        if len(resumo) > 500:
            raise Exception('Resumo não pode ter mais de 500 caracteres')
        self.__resumo = resumo

    def _set_sumario(self, sumario):
        if sumario in [None, '', ' ']:
            raise Exception("Sumario não pode ser nulo")
        self.__sumario = sumario

    def _set_preco(self, preco):
        if preco in [None]:
            raise Exception("preco não pode ser Nulo")
        if preco < 20:
            raise Exception("Preço não pode ser inferior a 20 reias")
        self.__preco = preco

    def _set_num_paginas(self, num_paginas):
        if num_paginas in [None]:
            raise Exception("Numera de pagina não pode ser Nulo")
        if num_paginas < 100:
            raise Exception("Numero de pagina não pode ser inferior a 100")
        self.__num_paginas = num_paginas

    def _set_isbn(self, isbn):
        if isbn in [None]:
            raise Exception("isbn não pode ser Nulo")
        self.__isbn = isbn

    def _set_data(self, data):
        if not self._data_valida(data):
            raise Exception("Data deve ser futura {}".format(data))
        self.__data = data

    def _set_categoria(self, categoria):
        if categoria in [None]:
            raise Exception("categoria não pode ser Nulo")
        self.__categoria = categoria
    
    def _data_valida(self, data_str):
        #tranforma string no objeto da classe Date
        data = datetime.strptime(data_str, '%d/%m/%Y').date()
        hoje = datetime.today().date()
        return data >= hoje