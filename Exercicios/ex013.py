print('Bônus salarial')
s = float(input('Digite seu salário: R$'))
#a = s * 1.15
a = s + (s * 15/100)
print('\n Você recebe {} \n Você receberá {:.2f} reais, após o bônus de 15%'.format(s, a))
