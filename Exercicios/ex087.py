'''matriz = [[], [], []]
somapar = soma3 = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if j == 2:
            soma3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma dos valores da terceira coluna: {soma3}')
print(f'O maior valor da segunda linha é: {maior}')'''

matriz = [[0]*3, [0]*3, [0]*3]
spar = scol = mai = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j]
    print()
print('-='*30)
print(f'Soma dos pares: {spar}')
for i in range(0, 3):
    scol += matriz[i][2]
print(f'A soma da 3ª coluna é: {scol}')
for j in range(0, 3):
    if matriz[1][j] > mai or j == 0:
        mai = matriz[1][j]
print(f'O maior da 2ª linha é: {mai}')