'''print('10 primeiros termos de uma pa mais alguns!')
a1 = int(input('Digite o primeiro termo da pa: '))
r = int(input('Digite a razão da pa: '))
c = 0
while c != 10:
    if c == 9:
        print(f'{a1 + c*r}')
    else:
        print(f'{a1 + c*r}, ', end='')
    c += 1
extras = int(input('Quer calcular mais quantos termos? Digite 0 para parar: '))
while extras != 0:
    while extras > 0:
        if extras != 1:
            print(f'{a1 + c*r}, ', end='')
        else:
            print(f'{a1 + c*r}, Pausa')
        extras -= 1
        c += 1
    extras = int(input('Quer calcular mais quantos termos? Digite 0 para parar: '))
print('Fim!')
print('Foram calculados no total {} termos!'.format(c))
'''
'''a1 = int(input('a1: '))
r = int(input('r: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{a1}, ', end='')
        a1 += r
        cont += 1
    print('fim')
    mais = int(input('quer ver mais quantos? digite 0 para parar: '))
print(f'voce visualizou {total} termos!')
'''
