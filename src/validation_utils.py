from datetime import datetime
import re
from typing import Union
from validate_docbr import CPF as validade_CPF  # type: ignore


def eh_nulo_ou_vazio(valor: Union[str, int, float]) -> bool:
    return valor in [None, '', ' ']


def valida_se_data_futura(data_str: str) -> bool:
    # tranforma string no objeto da classe Date
    data = datetime.strptime(data_str, '%d/%m/%Y').date()
    hoje = datetime.today().date()
    return data >= hoje


def valida_email(email: str) -> bool:
    regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    # verifica se email eh valido
    if re.search(regex, email):
        return True
    return False


def valida_CPF(CPF: str) -> bool:
    return validade_CPF().validate(CPF)
