'''print('fibonacci')
termos = int(input('Digite a quantidade de termos: '))
t1 = 0
t2 = 1
print(f'{t1}, {t2}, ', end='')
while termos > 0:
    t3 = t1 + t2
    print(t3, end=', ')
    termos -= 1
    t1 = t2
    t2 = t3
print('fim')'''
'''print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Digite um número inteiro: '))
c = 3
t1 = 0
t2 = 1
print(f'Os {n} primeiros termos na sequencia de fibonacci são:')
print('~'*30)
print(f'{t1}, {t2}, ', end='')
while c <= n:
    t3 = t1 + t2
    print(t3, end=', ')
    c += 1
    t1 = t2
    t2 = t3
print('Fim')
print('~'*30)'''

'''n= int(input("numero"))
lista=[1,1]
for i in range(n-2):
      lista.append(lista[-1]+lista[-2])
print(lista)'''

Nant = 1
Fibonacci = 0
n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))
while n >= 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci += Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')

