print('Análise de vogais!\n')
palavras = ('estudar', 'aprender', 'malhar', 'correr', 'subir', 'gargarejar', 'sentar', 'comer', 'lançar', 'jogar',
            'sair', 'entrar', 'digitar', 'olhar')

'''vogais = ('a', 'e', 'i', 'o', 'u')
for c in range(0, 14):
    print(f'\nA palavra {palavras[c].upper()} tem vogais: ', end='')
    for i in range(0, 5):
        if vogais[i] in palavras[c]:
            print(vogais[i], end=' ')'''

'''vogais = ('a', 'e', 'i', 'o', 'u')
for pal in palavras:
    print(f'\nA palavra {pal.upper()} tem vogais: ', end='')
    for vog in vogais:
        if vog in pal:
            print(vog, end=' ')'''

for pala in palavras:
    print(f'\nNa palavra {pala.upper()} temos as vogais: ', end='')
    for letra in pala:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
