print('\033[34mFrases\033[m')
frs = str(input('Digite uma frase qualquer: ')).strip()
a = frs.upper().count('A')
a_f = frs.lower().find('a') + 1
a_l = frs.upper().rfind('A') + 1
print('A letra \033[4;32m"A"\033[m aparece {} vezes\n'
      'Ela aparece pela primeira vez na posição: {}{}{}'
      '\nPela última vez na posição: {}{}{}'
      .format(a, '\033[35m', a_f, '\033[m', '\033[33m', a_l, '\033[m'))
