'''print('Progressão Aritmética com while')
a1 = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão: '))
c = 0
print('Os 10 primeiros termos da preogressão são: ')
while c != 10:
    if c == 9:
        print(f'{a1 + c*r}')
    else:
        print(f'{a1 + c*r}, ', end='')
    c += 1'''
a1 = int(input('Digite o 1 termo: '))
r = int(input('Digite a razão: '))
c = 1
termo = a1
while c <= 10:
    print(f'{termo}', end=' -> ')
    termo += r
    c += 1
print('Fim')

