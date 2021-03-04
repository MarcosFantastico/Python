'''print('Fatorial com for!')
n = int(input('Digite um número: '))
fatorial = 1
print(f'{n}! = ', end='')
for cont in range(n, 0, -1):
    if cont != 1:
        print(f'{cont} X ', end='')
    else:
        print(cont)
    fatorial *= cont
print(f'O fatorial de {n} é: {fatorial}')'''

print('fatorial')
n = int(input('Digite um n para calcular o fatorial: '))
fatorial = n
for c in range(n, 0, -1):
    print(c, end='')
    print(' X ' if c > 1 else ' = ', end='')
    if c > 1:
        c -= 1
    fatorial *= c
print(fatorial)
