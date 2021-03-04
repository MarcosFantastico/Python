"""
from math import pow, sqrt
print('Calculando hipotenusa')
cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
hipo = sqrt(pow(cat1, 2) + pow(cat2, 2))
print('O triângulo retângulo de cateto oposto = {} e cateto adjacente = {}\n'
      'tem como hipotenusa o valor: {:.2f}'.format(cat1, cat2, hipo))

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
"""
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa mede {}'.format(hi))

