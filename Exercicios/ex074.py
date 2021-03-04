'''from random import randint
print('\033[97mNúmeros aleatórios!\033[m')
pc = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('A lista gerada é:')
print(pc)
print(f'O menor valor é: {min(pc)}')
print(f'O maior valor é: {max(pc)}')'''

from random import randint
pc = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('Lista gerada:')
for i in pc:
    print(i, end=' ')
c = 4
menor = maior = 0
while c >= 0:
    if c == 4:
        maior = menor = pc[c]
    else:
        if pc[c] < menor:
            menor = pc[c]
        elif pc[c] > maior:
            maior = pc[c]
    c -= 1
print(f'\nO maior número é: {maior}')
print(f'O menor número é: {menor}')
