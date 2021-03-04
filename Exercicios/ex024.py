print('Cidade SANTO')
cidade = str(input('Digite o nome da cidade: ')).strip()
snt = cidade[:5].upper() == 'SANTO'
print('A cidade começa com "SANTO"? {}'.format(snt))
