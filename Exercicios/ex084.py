'''dado = list()
pessoas = list()
pesadas = []
leves = []
cont = pesado = leve = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    cont += 1
    if cont == 1:
        pesado = dado[1]
        leve = dado[1]
    elif dado[1] > pesado:
        pesado = dado[1]
    elif dado[1] < leve:
        leve = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
for c in pessoas:
    if c[1] == pesado:
        pesadas.append(c[0])
    if c[1] == leve:
        leves.append(c[0])
print(f'Foram cadastradas {cont} pessoas')
print('Os mais pesadas são: ', end='')
for i in range(0, len(pesadas)):
    print(f'{pesadas[i]}, ' if i < len(pesadas)-1 else f'{pesadas[i]}.', end='')
print(f' Essas pessoas pesam: {pesado}Kgs')
print('Os mais leves são: ', end='')
for pos, pes in enumerate(leves):
    print(f'{pes}, ' if pos < len(leves)-1 else f'{pes}.', end='')
print(f' Essas pessoas pesam: {leve}Kgs')'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    elif temp[1] > mai:
        mai = temp[1]
    elif temp[1] < men:
        men = temp[1]
    princ.append(temp[:])
    temp.clear()
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if conti == 'N':
        break
print('Ao todo foram cadastradas {} pessoas'.format(len(princ)))
print(f'O maior peso foi de {mai}Kg. Peso de: ', end='')
for pess in princ:
    if pess[1] == mai:
        print(f'{pess[0]}; ', end='')
print(f'\nO menor peso foi de {men}Kg. Peso de: ', end='')
for pess in princ:
    if pess[1] == men:
        print(f'{pess[0]}; ', end='')
