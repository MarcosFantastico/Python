print('Vários \033[1;97;42mnumeros\033[m!')
s = cont = 0
while True:
    n = int(input('Digite um número inteiro. [999 para parar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Voçê digitou {cont} termos e a soma entre eles é: {s}')
