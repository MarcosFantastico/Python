print('\033[93mMaior e menor\033[m')
n1 = float(input('\033[1;94mDigite o \033[32mprimero\033[m número: '))
n2 = float(input('\033[1;94mDigite o \033[33msegundo\033[m número: '))
n3 = float(input('\033[1;94mDigite o \033[95mterceiro\033[m número:'))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n2
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n2 and n3 < n1:
    menor = n3
print('O maior número é: {}{}{}\nO menor número é: {}{}{}'
      .format('\033[92m', maior, '\033[m', '\033[91m', menor, '\033[m'))
