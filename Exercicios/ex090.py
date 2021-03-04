from emoji import emojize
print('Dicionário em python')
alunos = dict()
cores = {'verde': '\033[1;92m', 'amarelo': '\033[1;93m', 'vermelho': '\033[1;91m', 'limp': '\033[m'}
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = int(input(f'Média de {alunos["Nome"]}: '))
if alunos['Média'] < 6:
    alunos['Situação'] = \
        f'{emojize("{}:cry: Reprovado! :cry:{}".format(cores["vermelho"], cores["limp"]),use_aliases=True)}'
elif 7 > alunos['Média'] >= 6:
    alunos['Situação'] = f'{emojize("{}:expressionless_face: Recuperação! :expressionless_face:{}".format(cores["amarelo"], cores["limp"]), use_aliases=True)}'
elif alunos['Média'] >= 7:
    alunos['Situação'] = \
        f'{emojize("{}:birthday: Aprovado! :birthday:{}".format(cores["verde"], cores["limp"]), use_aliases=True)}'
for k, v in alunos.items():
    print(f'{k} é igual a: {v}')
