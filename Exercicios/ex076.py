print('=' * 40)
print(f'{" LISTAGEM DE PREÇOS ":^40}')
print('=' * 40)
produtos = ('Lapis', 1.50, 'Borracha', 1.00, 'Cola', 4.69, 'Caderno', 3.50, 'Mochila', 120.30)

'''print(f'{produtos[0]:.<30}R${produtos[1]:>7.2f}\n{produtos[2]:.<30}R${produtos[3]:>7.2f}\n{produtos[4]:.<30}R$'
      f'{produtos[5]:>7.2f}\n{produtos[6]:.<30}R${produtos[7]:>7.2f}\n{produtos[8]:.<30}R${produtos[9]:>7.2f}')'''

for pos, prod in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{prod:.<30}', end='')
    else:
        print(f'R${prod:>7.2f}')

'''for pos in range(0, 10):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')'''
print('=' * 40)
