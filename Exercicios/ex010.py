print('Conversor R$ para US$')
r = float(input('Digite quantos reais você possui: R$'))
d = r/5.31
e = r/6.43
y = r/0.051
print('Após a conversão de R${:.2f} você terá:\nUS${:.2f}'.format(r, d))
print('Ou €{:.2f}'.format(e))
print('Ou ¥{:.2f}'.format(y))
print('\nCondiderando\nUS$1 = R$5.31;\n1€ = R$6.43\n1¥ = R$0.051')
