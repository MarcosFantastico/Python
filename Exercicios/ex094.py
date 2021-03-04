from emoji import emojize
print('Unindo dicionários e listas')
pessoas = list()
listidade = list()
listaf = list()
dados = dict()
totidade = 0
while True:
    print('=='*15)
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F')
    if dados['sexo'] == 'F':
        listaf.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    totidade += dados['idade']
    pessoas.append(dados.copy())
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Erro! Digite apenas S ou N')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
media = totidade / len(pessoas)
for pess in pessoas:
    if pess['idade'] >= media:
        listidade.append(pess)
print('=='*20)
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'A média de idade do grupo é: {media:.2f} anos')
print(f'Lista das mulheres cadastradas: ', end='')
for pos, pes in enumerate(listaf):
    print(f'{pes}, ' if pos < len(listaf)-1 else f'{pes}.', end='')
print(f'\nLista das pessoas com idade acima ou igual a média: ')
for c in listidade:
    for k, v in c.items():
        print(emojize(f'{k} :arrow_right: {v}; ', use_aliases=True), end='')
    print()
print('<< FIM >>')
