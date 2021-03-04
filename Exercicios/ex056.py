print('Informações sob amostra')
media = 0
maior_idade_h = 0
mais_velho_h = ''
s = 0
contador_f = 0
for c in range(1, 5):
    print('----- {}ª Pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    s += idade
    if sexo in 'Mm':
        if idade > maior_idade_h:
            maior_idade_h = idade
            mais_velho_h = nome
    elif sexo in 'Ff':
        if idade < 20:
            contador_f += 1
media = s / 4
print(f'''A média da idade do grupo é: {media}
O homem mais velho é tem {maior_idade_h} anos e se chama: {mais_velho_h}
Quantidade de mulheres com menos de 20 anos: {contador_f}''')
