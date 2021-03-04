print('Varios números!')
lista = list()
while True:
    lista.append(int(input('Digite um número: ')))

    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
listapar = list()
listaimpar = list()
for pos, elem in enumerate(lista):
    if elem % 2 == 0:
        listapar.append(elem)
    elif elem % 2 == 1:
        listaimpar.append(elem)
print('Lista:')
print(lista)
print('Lista de pares: ')
print(listapar)
print('Lista de ímpares: ')
print(listaimpar)
