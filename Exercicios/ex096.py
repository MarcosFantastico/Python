def area(c, h):
    a2 = c * h
    print(f'A área do terreno {c} X {h} são: {a2}m²')


def linha():
    print('--'*12)


print('Função que calcula área')
linha()
print('Controle de Terrenos')
linha()
comprimento = float(input('Comprimento (m): '))
altura = float(input('Altura (m): '))
area(comprimento, altura)
