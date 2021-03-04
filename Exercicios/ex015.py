print('Aluguel de carros')
d = int(input('Digite quantos dias alugados: '))
km = float(input('Digite quantos Km rodados: '))
t = d * 60 + km * 0.15
print('O valor total a pagar é: R${:.2f}'.format(t))
print('Considerando R$60 ao dia e R$0.15 por Km rodado')
