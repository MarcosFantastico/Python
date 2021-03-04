print('Escrita por extenso!')
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = ' '
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número: {extenso[n]}')
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        print('Tente novamente..', end='')
    continuar = ' '
print('Fim. Volte sempre!')

'''extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while True:
    while n not in range(0, 21):
        n = int(input('Tente novamente... Digite um número entre 0 e 20: '))
    break
print(f'Você digitou o número: {extenso[n]}')'''
