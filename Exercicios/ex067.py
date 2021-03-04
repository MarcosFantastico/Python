from emoji import emojize
print(emojize(':symbols:\033[94mTabuada!\033[m:symbols:', use_aliases=True))
cont = 0
while True:
    n = int(input('Digite um número para calcular a tabuada: '))
    print('-' * 30)
    if n < 0:
        break
    while cont <= 10:
        print(f'{cont:2} X {n} = {cont * n}')
        cont += 1
    print('-' * 30)
    cont = 0
print('FIM. Volte sempre')

'''while True:
    n = int(input('Digite um n para calcular a tabuada: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c:2} = {n*c}')
print('fim')'''
