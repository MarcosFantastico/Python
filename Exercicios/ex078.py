print('\033[97;44mGuardando valores em listas! (maior e menor valor)\033[m')
lista = list()
listamaior = list()
listamenor = list()
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c + 1}º valor da lista: ')))
    if c == 0:
        maior = menor = lista[c]
    elif lista[c] < menor:
        menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
'''for pos, vals in enumerate(lista):
    print(f'{vals}', end=' ')
    if maior == vals:
        listamaior.append(pos)
    if menor == vals:
        listamenor.append(pos)
print(f'\nO maior valor encontrado foi {maior} nas posições: {listamaior}'
      'O menor valor encontrado foi {menor} nas posições: {listamenor}')'''
print(f'\nO maior valor encontrado foi {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if maior == v:
        print(i, end='...')
print(f'\nO menor valor encontrado foi {menor} nas posições: ', end='')
for i, v in enumerate(lista):
    if menor == v:
        print(i, end='...')
