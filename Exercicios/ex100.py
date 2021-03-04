from random import randint
from time import sleep
lista = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]


def sorteia():
    print(f'Sorteando {len(lista)} valores da lista: ', end='')
    for c in lista:
        print(f'{c}, 'if lista.index(c) < len(lista)-1 else f'{c}. ', end='')
        sleep(0.4)
    print('Pronto!')


def somapar():
    totpar = 0
    for c in lista:
        if c % 2 == 0:
            totpar += c

    print(f'Somando os valores pares de {lista} temos: {totpar}')


sorteia()
somapar()
