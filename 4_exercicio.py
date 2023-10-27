"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Diga seu nome? ')
idade = input('Diga sua idade? ')
espaco = ' '

if (espaco not in nome) and (espaco not in idade):
    print('Desculpa, você deixou campos vazios')

elif nome:
    print('--' * 10)

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é ({nome[::-1]})')

    print('--' * 10)

    print('A primeira letra do seu nome é', nome[0])
    print('A ultima letra do seu nome é', nome[-1])

    print('--' * 10)

    if nome in 'n':
        print('Seu nome contém a letra n')
    else:
        print('Seu nome não contém a letra n')

    print('--' * 10)

    if espaco not in nome:
        print('Seu nome não contém espaço')
    else:
        print('Seu nome contém espaço')
