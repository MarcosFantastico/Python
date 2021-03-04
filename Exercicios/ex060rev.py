n = int(input('Digite um n para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

'''print('Fatoriais!')
n = int(input('Digite um número: '))
fatorial = n
print(f'O fatorial de {n} é: ')
print(f'{n}! = {n}', end='')
while n != 1:
    n -= 1
    fatorial *= n
    print(f' X {n}', end='')
print(f' = {fatorial}')'''

'''from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''
