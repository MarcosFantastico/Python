import datetime
cores = {'ver': '\033[1;92m', 'am': '\033[1;93m', 'verm': '\033[1;91m', 'lim': '\033[m'}
print('{}Alistamento Militar!{}'.format(cores['ver'], cores['lim']))
sex = str(input('Digite o seu sexo: [ F ] / [ M ]: '))
escolha = ''
if sex == 'F':
    print('Olha, pessoas do sexo feminino não precisam fazer o alistamento \033[1;93mOBRIGATÓRIO\033[m!')
    escolha = str(input('Se quiser continuar mesmo assim \033[1;92mdigite [ 1 ]\033[m: '))

if escolha == '1' or sex == 'M':
    nasc = int(input('Informe a data de nascimento: '))
    anoatual = datetime.date.today().year
    idade = anoatual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, anoatual))
    if idade < 18:
        saldo = 18 - idade
        anoalis = anoatual + saldo
        print('Você ainda irá se alistar ao serviço militar! {}{} anos{} restantes!'
              .format(cores['ver'], saldo, cores['lim']))
        print('\033[1;92mSeu alistamento será em {}\033[m'.format(anoalis))
    elif idade == 18:
        print('{}Já esta na hora de se alistar!{}'.format(cores['am'], cores['lim']))
    else:
        saldo = idade - 18
        anoalis = anoatual - saldo
        print('Você já deviria ter se alistado há {}{} anos{}!'.format(cores['verm'], saldo, cores['lim']))
        print('\033[1;91mSeu alistamento foi em {}\033[m'.format(anoalis))
