'''print('Viagens')
km = float(input('Digite a quantidade de km de sua viagem: '))
if km <= 200:
    tot = km * 0.5
else:
    tot = km * 0.45
print('O total de sua viagem é: R${:.2f}'.format(tot))'''
print('\033[1;30;44m-)(-\033[m' * 20)
print('{:^80}'.format('\033[35mViagens!!!\033[m'))
print('\033[1;30;44m-)(-\033[m' * 20)
distancia = float(input('Digite a distância da sua viagem: '))
total = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('O total a pagar será de: {}R${:.2f}{}'.format('\033[1;33m', total, '\033[m'))

