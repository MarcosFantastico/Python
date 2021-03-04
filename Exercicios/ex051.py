'''from emoji import emojize
print(emojize(':ten:PA de 10 termos!:ten:', use_aliases=True))
a1 = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da PA: '))
print(emojize('Os :ten: primeiros termos dessa PA são:', use_aliases=True))
for c in range(0, 10):
    print(a1 + c*r, end=' -> ')
print('fim')'''

from emoji import emojize
print(emojize(':ten:PA de 10 termos!:ten:', use_aliases=True))
a1 = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da PA: '))
print(emojize('Os :ten: primeiros termos dessa PA são:', use_aliases=True))
decimo = a1 + (10 - 1) * r
for c in range(a1, decimo + r, r):
    print(f'{c}', end=', ')
print('fim')
