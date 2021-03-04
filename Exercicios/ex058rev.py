'''from random import randint
print('\033[34m=+=\033[m' * 10)
print(f'\033[97m{"Tente adivinhar 2!":^30}\033[m')
print('\033[34m=+=\033[m' * 10)
computador = randint(0, 10)
contador = 1
jogador = int(input('Já pensei em um número entre 0 e 10, adivinhe! '))
while computador != jogador:
    if jogador < computador:
        jogador = int(input('\033[31mErrado!\033[m Tente novamente(...Um pouco mais!): '))
    elif jogador > computador:
        jogador = int(input('\033[31mErrado!\033[m Tente novamente(...Um pouco menos!): '))
    contador += 1
print(f'\033[32mParabéns voce acertou!\033[m\nForam necessárias \033[1;93m{contador}\033[m tentativas para acertar!')
'''
from random import randint
print('Tente advinhar 2!')
computador = randint(0, 10)
print('Já pensei em um número entre 0 e 10!\nSerá que você consegue acertar?')
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
        print('Parabéns voce acertou!')
    else:
        if jogador < computador:
            print('Mais... Digite seu palpite: ')
        elif jogador > computador:
            print('Menos... Digite seu palpite: ')
print(f'Você acertou com {tentativas} tentativas')
