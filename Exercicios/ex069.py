print('Idade e Sexo!')
cont_idad = cont_M = cont_menor = 0
while True:
    print(f'{" Cadastre uma pessoa ":=^40}')
    idad = int(input('Digite sua idade: '))
    sex = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    while sex not in 'MF':
        print('\033[91mSexo Inválido!!!\033[m Cadastre-o novamente!')
        sex = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if idad > 18:
        cont_idad += 1
    if sex in 'M':
        cont_M += 1
    elif sex in 'F':
        if idad < 20:
            cont_menor += 1
    flag = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while flag not in 'SN':
        flag = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if flag == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'''Pessoas com mais de 18 anos: {cont_idad}
Homens cadastrados: {cont_M}
Mulheres menores de 20 anos: {cont_menor}''')
