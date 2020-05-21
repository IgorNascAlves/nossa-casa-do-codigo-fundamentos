from datetime import datetime

from typing import Union


def eh_nulo_ou_vazio(valor: Union[str, int, float]) -> bool:
    return valor in [None, '', ' ']


def valida_se_data_futura(data_str):
    # tranforma string no objeto da classe Date
    data = datetime.strptime(data_str, '%d/%m/%Y').date()
    hoje = datetime.today().date()
    return data >= hoje
