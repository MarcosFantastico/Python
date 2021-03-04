print('\033[4;31;43mOlá, Mundo!\033[m')
print('\033[0;30;45mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[0;33m{}\033[m e \033[0;32m{}\033[m'.format(a, b))
nome = 'Marcos'
print('Olá! Prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

coresansi = {'limpa': '\033[m',
             'preto': '\033[30m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m',
             'magenta': '\033[35m',
             'ciano': '\033[36m',
             'cinza claro': '\033[37m',
             'cinza escuro': '\033[90m',
             'vermelho claro': '\033[91m',
             'verde claro': '\033[92m',
             'amarelo claro': '\033[93m',
             'azul claro': '\033[94m',
             'magenta claro': '\033[95m',
             'ciano claro': '\033[96m',
             'branco': '\033[97m'}

print('Olá {}{}{}!'.format(coresansi['magenta'], nome, coresansi['limpa']))
