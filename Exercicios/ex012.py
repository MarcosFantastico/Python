print('Descontos')
p = float(input('Digite o preço do produto para calcular o desconto: R$'))
d = p * 0.95
# Ou d = p - (p * 5 / 100)
print('O valor após 5% de desconto é: {:.2f}'.format(d))
