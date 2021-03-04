from random import choice
cores = {'azul claro': '\033[94m',
         'amarelo claro': '\033[93m',
         'magenta claro': '\033[95m',
         'vermelho claro': '\033[91m',
         'verde claro': '\033[92m',
         'limpa': '\033[m'}
print('Sorteio')
aluno1 = str(input('{}Digite o nome do seu 1º aluno:{} '.format(cores['azul claro'], cores['limpa'])))
aluno3 = str(input('{}O nome do 2º: {}'.format(cores['magenta claro'], cores['limpa'])))
aluno2 = str(input('{}O nome do 3º: {}'.format(cores['amarelo claro'], cores['limpa'])))
aluno4 = str(input('{}O nome do 4º: {}'.format(cores['verde claro'], cores['limpa'])))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('A pessoa escolhida foi: {}"{}"{}'.format(cores['vermelho claro'], escolhido.upper(), cores['limpa']))
