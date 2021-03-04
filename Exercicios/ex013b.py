print('Transações')
pr = float(input('Digite o valor do produto desejado: R$'))
desc = pr - (pr * 12/100)
a = pr + (pr * 8 / 100)
print('Se for pago a vista, o produto que antes custava R${:.2f} com 12% de desconto agora custa R${:.2f}'
      '\nParcelando de 2 ou mais vezes o produto que custava R${}, custará R${} devido ao aumento de 8%'
      .format(pr, desc, pr, a))
