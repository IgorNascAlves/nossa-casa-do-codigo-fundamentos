from src.autor import Autor

lista_autores = []
lista_autores.append(Autor('Igor',
                           'igor.nascimento@caelum.com.br',
                           'Estudante de Python e ML'))
lista_autores.append(Autor('Thiago',
                           'thiago@hotmail.com',
                           'Estudante de Java'))
lista_autores.append(Autor('Cassio',
                           'cassio@yahoo.org',
                           'Estudante de JavaScript'))

for item in lista_autores:
    print(item)
