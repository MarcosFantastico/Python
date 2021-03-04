print('Números!')
continuar = ''
cont = soma = maior = menor = 0
while continuar != 'N':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    continuar = str(input('Quer continuar? [S / N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Valor inválido, tente novemente [S / N]: ')).upper().strip()[0]
media = soma / cont
print(f'''Números digitados: {cont}
Média: {media}
Maior: {maior}
Menor: {menor}''')
