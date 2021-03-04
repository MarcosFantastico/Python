print('boltim com notas!')
'''dados = []
alunos = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1]+dados[2])/2)
    alunos.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 15)
print(f'{"No."} {"Nome"}{"Média":>20}')
print('-' * 30)
for pos, alu in enumerate(alunos):
    print(f'{pos:<4}{alu[:][0]:<14}{alu[:][3]:>10.1f}')
while True:
    notas = -1
    while notas not in range(0, len(alunos)):
        notas = int(input('Mostrar notas de qual aluno? (999) para parar: '))
        if notas in range(0, len(alunos)):
            break
        elif notas == 999:
            break
        else:
            print('\033[1;91mParâmetros inválidos! \033[m', end='')
    if notas == 999:
        break
    print(f'As notas do aluno {alunos[notas][0]} são: {alunos[notas][1]} e {alunos[notas][2]}.')
print('Fim')'''
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print('-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>10}')
print('=' * 30)
for i, alu in enumerate(ficha):
    print(f'{i:<4}{alu[0]:<10}{alu[2]:>10.1f}')
while True:
    notas = int(input('Quer ver as notas de qual aluno? (999 para parar): '))
    if notas == 999:
        break
    elif 0 <= notas <= len(ficha) - 1:
        print(f'As notas de {ficha[notas][0]} são: {ficha[notas][1]}')
    else:
        print('\033[91mDados inválidos...\033[m', end='')
print('Fim')
