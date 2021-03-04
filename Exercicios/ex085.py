vals = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        vals[0].append(num)
    elif num % 2 == 1:
        vals[1].append(num)
vals[0].sort()
vals[1].sort()
print(f'Valores pares: {vals[0]}')
print(f'Valores ímpares: {vals[1]}')
