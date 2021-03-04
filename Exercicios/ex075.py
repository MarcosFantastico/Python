'''print('Análise de números em uma tupla!')
valores = (int(input('Valor 1: ')), int(input('Valor 2: ')), int(input('Valor 3: ')), int(input('Valor 4: ')))
cont9 = 0
cont3 = 0
if 3 in valores:
    cont3 = valores.index(3) + 1
else:
    cont3 = '\033[91mNenhuma posição!\033[m'
pares = ()
for c in range(0, 4):
    if valores[c] == 9:
        cont9 += 1
    if valores[c] % 2 == 0:
        pares += (valores[c],)
if pares == ():
    pares = '\033[91mNenhum número par encontrado!\033[m'
print('Lista:')
for i in valores:
    print(i, end=' ')
print(f'\nO valor 9 apareceu \033[94m{cont9}\033[m vezes!')
# ou somente valores.count(9)
print(f'O 1º valor 3 aparece na posição: {cont3}')
print(f'Numeros pares digitados: {pares}')'''
valores = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')),
           int(input('Digite um último valor: ')))
print('lista:')
for c in valores:
    print(c, end=' ')
print(f'\nO valor 9 apareceu: {valores.count(9)} vezes')
print(f'O valor 3 aparece primeiramente na {valores.index(3)+1}ª posição' if 3 in valores else
      'O valor 3 não foi digitado!')
print('Números pares digitados: ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
