'''print('Banco')
valor = int(input('Digite o valor a ser sacado: R$'))
ced = 50
tot_ced = 0
while True:
    if valor >= ced:
        valor -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R${ced}')
        tot_ced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if valor == 0:
            break'''
'''from emoji import emojize
print(emojize('\033[92m:euro: :pound: Caixa eletrônico! :yen: :dollar:\033[m', use_aliases=True))
print('Notas:\nR$50.00;\nR$20.00;\nR$10.00 e;\nR$1.00.')
valor = int(input('Informe o valor a ser sacado: '))
n50 = n20 = n10 = n1 = 0
while valor // 50 > 0:
    n50 += 1
    valor -= 50
while valor // 20 > 0:
    n20 += 1
    valor -= 20
while valor // 10 > 0:
    n10 += 1
    valor -= 10
while valor // 1 > 0:
    n1 += 1
    valor -= 1
print(f'{" FIM DO PROGRAMA ":=^40}')
print('TOTAL DE NOTAS:')
if n50 > 0:
    print(f'Total de {n50} notas de 50')
if n20 > 0:
    print(f'Total de {n20} notas de 20')
if n10 > 0:
    print(f'Total de {n10} notas de 10')
if n1 > 0:
    print(f'Total de {n1} notas de 1')'''

