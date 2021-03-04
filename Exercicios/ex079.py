print(' Adicionando valores únicos na lista!')
lista = list()
while True:
    num = int(input('Digite o valor: '))
    if num not in lista:
        print('Valor adicionado...')
        lista.append(num)
    else:
        print('Valor duplicado, não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print('Valores digitados em ordem crescente: ', end='')
print(sorted(lista))
