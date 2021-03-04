from math import pow
print('\033[34mIMC\033[m')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / pow(altura, 2)
print('IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[1;31mAbaixo do peso!\033[m')
elif imc <= 25:
    print('\033[1;32mPeso ideal!\033[m')
elif imc <= 30:
    print('\033[1;91mSobrepeso!\033[m')
elif imc <= 40:
    print('\033[1;91mObesidade!\033[m')
else:
    print('\033[1;91mObesidade mórbida!\033[m')
