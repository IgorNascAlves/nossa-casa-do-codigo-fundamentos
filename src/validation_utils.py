from datetime import datetime, date


def is_null_empty(valor):
    return valor in [None, '', ' ']

def valida_se_data_futura(data_str):
    #tranforma string no objeto da classe Date
    data = datetime.strptime(data_str, '%d/%m/%Y').date()
    hoje = datetime.today().date()
    return data >= hoje