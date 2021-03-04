def escreva(txt):
    tamanho = len(txt)+4
    print('~'*tamanho)
    print(f'{txt:^{tamanho}}')
    # Ou print(f'  {txt}')
    print('~'*tamanho)


texto = str(input('Digite uma frase qualquer: '))
escreva(texto)
