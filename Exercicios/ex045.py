from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Escolha uma das opcões abaixo:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual sua jogada? '''))
if jogador < 0 or jogador > 2:
    print('Jogada inválida!')
else:
    print('\033[32mJO\033[m', end='')
    sleep(0.8)
    print('\033[33mKEN\033[m', end='')
    sleep(0.8)
    print('\033[34mPÔ\033[m')
    print('\033[35m-\033[m\033[36m=\033[m' * 15)
    print(f'O computador escolheu: {itens[computador]}')
    print(f'O jogador escolheu: {itens[jogador]}')
    print('\033[35m=\033[m\033[36m-\033[m' * 15)
    if computador == 0:
        if jogador == 0:
            print('Empate!')
        elif jogador == 1:
            print('Jogador vence!')
        elif jogador == 2:
            print('Computador vence!')
    elif computador == 1:
        if jogador == 0:
            print('Computador vence!')
        elif jogador == 1:
            print('Empate!')
        elif jogador == 2:
            print('Jogador vence!')
    elif computador == 2:
        if jogador == 0:
            print('Jogador vence!')
        elif jogador == 1:
            print('Computador vence!')
        elif jogador == 2:
            print('Empate!')

'''import random
import time
print('\033[95mJokenpô\033[m')
escolha = str(input('Vamos Jogar!\nDigite:\n- pedra;\n- papel ou;\n- tesoura: '))
print('\033[33mJO\033[m')
time.sleep(0.8)
print('\033[34mKEN\033[m')
time.sleep(0.8)
print('\033[35mPÔ!\033[m')
computador = ['pedra', 'papel', 'tesoura']
escolhacomputador = random.choice(computador)
print('-=-' * 14)
if (escolha == 'pedra' and escolhacomputador == 'pedra') or (escolha == 'papel' and escolhacomputador == 'papel') or \
        (escolha == 'tesoura' and escolhacomputador == 'tesoura'):
    print('\033[33mEmpate!\033[m\nVocê escolheu {} e eu escolhi {}!'.format(escolha, escolhacomputador))
elif (escolha == 'pedra' and escolhacomputador == 'tesoura') or (escolha == 'papel' and escolhacomputador == 'pedra')\
        or (escolha == 'tesoura' and escolhacomputador == 'papel'):
    print('\033[32mParabéns! Você venceu!\033[m\nVocê escolheu {} e eu escolhi {}'.format(escolha, escolhacomputador))
else:
    print('\033[31mEu venci!\033[m\nVocê escolheu {} e eu escolhi {}'.format(escolha, escolhacomputador))
print('=-=' * 14)'''
