from produto import Produto
from loja import Loja
from datetime import datetime
from livro import Livro
from cd import CD
from dvd import DVD

cmd = -1
while cmd:
    cmd = int(input('Menu:\n0 - Sair\n1 - Adicionar produto\n2 - Buscar por código\n3 - Buscar por nome\n4 - Vender produto\n5 - Listar produtos\n> '))
    if cmd == 1:
        tipo = int(input('\nTipo do produto:\n1 - Livro\n2 - CD\n3 - DVD\n> '))
        if (tipo < 1) or (tipo > 3):
            print('\nTipo invalido!\n')
            continue
        p: Produto
        codigo = int(input('\nCódigo: '))
        nome = input('Nome: ')
        estoque = int(input('Estoque: '))
        if tipo == 1:
            dataPublicacao = datetime.strptime(input('Data de publicação: '), '%d/%m/%Y')
            autor = input('Autor: ')
            genero = input('Genero: ')
            idioma = input('Idioma: ')
            p = Livro(codigo, nome, estoque, dataPublicacao, autor, genero, idioma)
        elif tipo == 2:
            atributoHipoteticoCD = input('Atributo hipotético CD: ')
            p = CD(codigo, nome, estoque, atributoHipoteticoCD)
        elif tipo == 3:
            atributoHipoteticoDVD = input('Atributo hipotético DVD: ')
            p = DVD(codigo, nome, estoque, atributoHipoteticoDVD)
        Loja.adicionar(p)
        print(f'\n{p.estoque} itens de {p.nome} foram adicionados\n')
    elif cmd == 2:
        try:
            p = Loja.buscarCodigo(int(input('\nCódigo: ')))
            print(f'\n{p}\n')
        except:
            print('\nProduto não encontrado!\n')
    elif cmd == 3:
        p = Loja.buscarNome(input('\nNome: '))
        if p == None:
            print('\nProduto não encontrado!\n')
        else:
            print(f'\n{p}\n')
    elif cmd == 4:
        try:
            p = Loja.vender(int(input('\nCódigo: ')))
            print(f'\n{p.estoque} itens de {p.nome} foram removidos\n')
        except:
            print('\nCódigo invalido!\n')
    elif cmd == 5:
        print(f'\n{Loja.listar()}\n')
    else:
        print()