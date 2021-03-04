from datetime import date
print('\033[94mAnos bissextos!\033[m')
ano = int(input('Digite o ano desejado, Coloque \033[4m0\033[m para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é bissexto'.format('\033[92m', ano, '\033[m'))
else:
    print('O ano {}{}{} não é bissexto'.format('\033[91m', ano, '\033[m'))
