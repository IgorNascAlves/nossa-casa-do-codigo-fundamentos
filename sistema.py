from src.livro import Livro
from src.colecaoLivro import ColecaoDeLivro
from src.carrinho import Carrinho

from datetime import datetime


colecao_de_livro = ColecaoDeLivro()
hoje_em_string = datetime.today().date().strftime('%d/%m/%Y')

livro1 = Livro("Machine Learning em COBOL",
               'M'*500, '<br> **** \n <html>'*50,
               30.20, 150, '978-3-16-148410-0',
               hoje_em_string, 'Machine Learning')
livro2 = Livro("Data Science em COBOL",
               'M'*500, '<br> **** \n <html>'*50,
               29.80, 150, '123-3-16-148410-0',
               hoje_em_string, 'Data Science')
livro3 = Livro("Mobile em COBOL",
               'M'*500, '<br> **** \n <html>'*50,
               55.20, 150, '456-3-16-148410-0',
               hoje_em_string, 'Mobile')

colecao_de_livro.incluir(livro1)
colecao_de_livro.incluir(livro2)
colecao_de_livro.incluir(livro3)

carrinho = Carrinho()

titulo1 = "Machine Learning em COBOL"
titulo2 = "Data Science em COBOL"
titulo3 = "Mobile em COBOL"

livro_retornado1 = colecao_de_livro.busca_livro(titulo1).pop()
livro_retornado2 = colecao_de_livro.busca_livro(titulo2).pop()
livro_retornado3 = colecao_de_livro.busca_livro(titulo3).pop()

carrinho.addLivro(livro_retornado1)
carrinho.addLivro(livro_retornado1)
carrinho.addLivro(livro_retornado1)

carrinho.addLivro(livro_retornado2)
carrinho.addLivro(livro_retornado3)

for titulo, detalhes in carrinho.lista.items():
    print(f'Titulo: {titulo} Qtd: {detalhes[0]} Preco: {detalhes[1]}')

r'''
PS D:\Documentos\GitHub\nossa-casa-do-codigo-fundamentos> python .\sistema.py
Titulo: Machine Learning em COBOL Qtd: 3 Preco: 30.2
Titulo: Data Science em COBOL Qtd: 1 Preco: 29.8
Titulo: Mobile em COBOL Qtd: 1 Preco: 55.2
'''
