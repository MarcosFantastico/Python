from random import randint
from time import sleep
print('\033[1;30;43m-=-\033[m' * 20)
print('{:' '^60}'.format('\033[34mTente adivinhar...\033[m'))
print('\033[1;30;43m-=-\033[m' * 20)
escolha = randint(0, 5)
print('Estou pensando em um número entre 0 e 5')
tentativa = int(input('Digite sua tentativa: '))
print('\033[1;35mProcessando...\033[m')
sleep(3)
if tentativa == escolha:
    print('\033[32mParabéns, você acertou!\033[m')
else:
    print('\033[31mNão foi dessa vez, tente novamente!\033[m')
print('O numero que escolhi foi o {}{}{}!'.format('\033[32m', escolha, '\033[m'))
