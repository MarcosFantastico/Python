'''print('Adicionando 5 valores!')
lista = list()
for c in range(0, 5):
    n = int(input('Digite o valor: '))
    if c == 0:
        lista.append(n)
        print(f'Valor adicionado na posição {c}')
  # elif n > lista[len(lista)-1]:
    elif n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos <= len(lista)-1:
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('Valores em ordem:')
print(lista)'''
