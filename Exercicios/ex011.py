print('Calculando área')
c = float(input('Digite o comprimento da parede: '))
h = float(input('Digite a altura da parede: '))
a = c * h
li = a / 2
print('\nA parede de dimensão {}x{} tem {:.2f}m² de área\n'
      'Serão necessários {:.2f} litros de tinta para pintar a parede !'.format(c, h, a, li))
