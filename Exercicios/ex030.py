print('Par ou Ímpar')
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número é \033[7mpar!\033[m')
else:
    print('O número é \033[97mímpar!\033[m')
