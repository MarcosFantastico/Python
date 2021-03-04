print('\033[95mSexos: \033[m')
sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[1;91mERRO!\033[m Favor informar um valor dentro dos parametros [M / F]: ')).strip().upper()[0]
print('Fim. Sexo {} registrado!'.format(sexo))
