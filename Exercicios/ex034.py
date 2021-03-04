'''print('Salários')
sal = float(input('Digite o salário: R$'))
if sal > 1250:
    sal *= 1.1
    print('Seu salário será de R${:.2f}'.format(sal))
else:
    sal *= 1.15
    print('Seu salário será de R${:.2f}'.format(sal))'''
salario = float(input('\033[4;91mDigite o salário:\033[m R$'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem antes ganhava {}R${:.2f}{}, passa a ganhar: {}R${:.2f}{}'
      .format('\033[93m', salario, '\033[m', '\033[91m', novo, '\033[m'))
