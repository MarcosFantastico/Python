import datetime
print('\033[94mConfederação Nacional de Natação\033[m')
nasc = int(input('Informe o ano de nascimento do atleta: '))
dataatual = datetime.date.today().year
idade = dataatual - nasc
print('O atleta tem: {} anos'.format(idade))
print('Classificação: ', end='')
if idade <= 9:
    print('{}MIRIM{}'.format('\033[1;30;101m', '\033[m'))
elif idade <= 14:
    print('{}INFANTIL{}'.format('\033[1;30;103m', '\033[m'))
elif idade <= 19:
    print('{}JUNIOR{}'.format('\033[1;30;102m', '\033[m'))
elif idade <= 25:
    print('{}SÊNIOR{}'.format('\033[1;30;104m', '\033[m'))
else:
    print('{}MASTER{}'.format('\033[1;30;105m', '\033[m'))
