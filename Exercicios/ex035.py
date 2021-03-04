print('\033[95;40m-=-\033[m' * 30)
print('{:^90}'.format('\033[1;94mAnalisador de triângulos\033[m'))
print('\033[95;40m-=-\033[m' * 30)
c1 = float(input('\033[34mDigite o comprimento da primeira reta: \033[m'))
c2 = float(input('\033[32mDigite o comprimento da segunda reta: \033[m'))
c3 = float(input('\033[33mDigite o comprimento da terceira reta: \033[m'))
if c1 + c2 > c3 and c2 < c1 + c3 and c1 < c2 + c3:
    print('\033[1;92mOs segmentos acima PODEM formar um triângulo\033[m')
else:
    print('\033[1;91mOs segmentos acima NÃO PODEM um triângulo\033[m')
