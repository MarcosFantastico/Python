'''matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()'''
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz = [[0] * 3, [0] * 3, [0] * 3]
print(matriz)
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

'''li = [[], [], []]
for c in range(1, 10):
    while True:
        try:
            if c < 4:
                n = int(input(f'\033[30;1mDigite um valor para a posição [1, {c}]: '))
                li[0].append(n)
            elif c < 7:
                n = int(input(f'Digite um valor para a posição [2, {c - 3}]: '))
                li[1].append(n)
            else:
                n = int(input(f'Digite um valor para a posição [3, {c - 6}]: '))
                li[2].append(n)
            break
        except ValueError:
            print('\033[31mDigite um valor válido.\033[30m')
print(f'\n\033[35mSua Matriz 3x3:{"_" * 20}\033[30m'
      f'[ {li[0][0]} ] [ {li[0][1]} ] [ {li[0][2]} ]'
      f'[ {li[1][0]} ] [ {li[1][1]} ] [ {li[1][2]} ]'
      f'[ {li[2][0]} ] [ {li[2][1]} ] [ {li[2][2]} ]')
'''