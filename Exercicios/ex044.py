print(f'\033[92m{" Compras! ":=^40}\033[m')
preco = float(input('Digite o preço do produto: '))
escolha = int(input('Escolha a opção de pagamento;'
                    '\n1 - À vista dinheiro/cheque (10% de desconto);'
                    '\n2 - À vista cartão (5% de desconto);'
                    '\n3 - 2x no cartão'
                    '\n4 - 3x ou mais no cartão(20% de jurus): '))
if escolha == 1:
    preco = preco - (preco * 10 / 100)
    print('O total é de R${} com \033[32m10% de desconto!\033[m'.format(preco))
elif escolha == 2:
    preco = preco - (preco * 5 / 100)
    print('O total a pagar é de R${} com \033[32m5% de desconto!\033[m'.format(preco))
elif escolha == 3:
    print('O total a pagar é de \033[33m{}!\033[m em 2x no cartão!'.format(preco))
elif escolha == 4:
    preco = preco + (preco * 20 / 100)
    parcelas = int(input('Digite a quantidade de parcelas: '))
    mes = preco / parcelas
    print('''O total a pagar é R${:.2f} ao mes, com \033[31m20% de jurus!\033[m. 
Totalizando \033[1;91mR${:.2f}\033[m em {} meses'''.format(mes, preco, parcelas))
else:
    print('\033[1;91mErro! Digite uma opcão de pagamento válida!!!\033[m')
