from random import randint
from emoji import emojize
print(emojize(':two: \033[95mPar\033[m ou \033[94mÍmpar\033[m! :three:', use_aliases=True))
print('\033[42;97mJogue até perder!\033[m')
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número: '))
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print('-' * 30)
    print(f'Você escolheu {jogador} o computador escolheu {computador} a soma é {soma}\n'
          f'O resuldado deu ', end='')
    print('Par!' if soma % 2 == 0 else 'Impar!')
    print('-' * 30)
    if escolha == 'I' and soma % 2 == 0:
        break
    elif escolha == 'P' and soma % 2 != 0:
        break
    cont += 1
    print('\033[1;42;97mVocê Venceu!\033[m')
    print('-' * 30)
print('\033[1;97;41mGame Over!!!\033[m')
print(f'Você ganhou {cont} vezes!')
print('FIM')
