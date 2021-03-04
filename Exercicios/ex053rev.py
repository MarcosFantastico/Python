'''print('Detector de Palíndromos!')
frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').upper()
tamanho = len(frase)
reverso = frase[tamanho::-1]
print(f'O inverso de {frase} é {reverso}')
if frase == reverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
'''
print('Detector de palíndromos!')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juncao = ''.join(palavras)
inverso = ''
for letra in range(len(juncao) - 1, -1, -1):
    inverso += juncao[letra]
print(f'Você digitou {frase} e o inverso é {inverso}')
if juncao == inverso:
    print('Temos um palíndromo!')
else:
    print('Não são palíndromos!')
