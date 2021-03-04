print('Leitor de números')
num = int(input('Digite um número de 0 a 9999: '))
un = num // 1 % 10
dz = num // 10 % 10
cn = num // 100 % 10
ml = num // 1000 % 10
print('O número {} tem:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num, un, dz, cn, ml))

'''from math import trunc
print('analisador de unidades')
num = int(input('Digite um valor entre 0 e 9999: '))
un = num / 1 % 10
dz = num / 10 % 10
cn = num / 100 % 10
ml = num / 1000 % 10
print('Un:{} \nDz:{} \nCn:{} \nMl:{}'.format(trunc(un), trunc(dz), trunc(cn), trunc(ml)))
'''