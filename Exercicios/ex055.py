from emoji import emojize
print(emojize('Pesos!:ramen:', use_aliases=True))
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'''O maior peso é: {maior:.1f}
O menor peso é: {menor:.1f}''')
