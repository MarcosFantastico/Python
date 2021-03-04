'''print('Números!')
n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número inteiro; Digite o valor 999 para parar: '))
    if n != 999:
        cont += 1
        soma += n
print(f'Você digitou {cont} números!\n
A soma entre eles é: {soma}')
'''
print('Números')
c = s = 0
n = int(input('Digite um número int. [999 para parar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número int. [999 para parar]: '))
print(f'A soma entre os números é: {s}\n'
      f'Você digitou {c} números!')
