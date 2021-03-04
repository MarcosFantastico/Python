from datetime import datetime
print('Cadastro de trabalhador em python')
info = dict()
info['nome'] = str(input('Nome: '))
nasc = int(input('Nascimento: '))
info['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
atual = datetime.now().year
info['idade'] = atual - nasc
if info['ctps'] > 0:
    info['contratação'] = int(input('Ano de contratação: '))
    anoaposen = info['contratação'] + 35
    anoscontrib = anoaposen - nasc - info['idade']
    info['salario'] = float(input('Salário: R$'))
    info['aposentadoria'] = info['idade'] + anoscontrib
for k, v in info.items():
    print(f'{k} tem o valor {v}')
