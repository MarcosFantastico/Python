"""
from random import sample
print('Sorteio ordenado')
aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('O nome do 3º: '))
aluno4 = str(input('O nome do 4ª: '))
ordem = sample([aluno1, aluno2, aluno3, aluno4], k=4)
print('A ordem de apresentação será: {}'.format(ordem))
"""
from random import shuffle
al1 = str(input('aluno 1: '))
al2 = str(input('aluno 2: '))
al3 = str(input('aluno 3: '))
al4 = str(input('aluno 4: '))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))
