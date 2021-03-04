print('\033[92mEmpréstimos\033[m!')
val = float(input('Digite o valor da casa: R$'))
sal = float(input('Informe o salário do comprador: R$'))
ano = int(input('Especifique em o tempo do financiamento: '))
mes = ano * 12
prest = val / mes
if prest > sal * 30 / 100:
    print('O valor da prestação exedeu 30% do seu salario totalizando R${:.2f}, empréstimo \033[91mNEGADO\033[m!'
          .format(prest))
else:
    print('Seu empréstimo foi \033[92mAPROVADO\033[m!\nO preço de cada prestação: R${:.2f}'
          '\nQuantidade de tempo: {} meses ou {} anos!'.format(prest, mes, ano))
