print('Produtos!')
total = cont_caro = cont = menor_p = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: R$'))
    if cont == 0 or preco < menor_p:
        menor_p = preco
        barato = nome
    total += preco
    cont += 1
    if preco > 1000:
        cont_caro += 1
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if flag == 'N':
        break
print(f'{"FIM DO PROGRAMA":=^40}')
print(f'''O total gasto foi de: R${total:.2f}
Total produtos de mais de R$1000,00: {cont_caro}
O produto mais barato é: {barato} que custa R${menor_p:.2f}''')
