'''print('Expressões!')
lista = list()
lista.append(str(input('Digite sua expressão: ')).strip())

paren_e = lista[0].count('(')
paren_d = lista[0].count(')')
if (paren_e + paren_d) % 2 == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão não é valida!')'''
'''exp = str(input('Digite sua expressão: '))
pilha = []
for paren in exp:
    if paren == '(':
        pilha.append('(')
    elif paren == ')':
        del(pilha[-1])
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')'''

'''exp = str(input('Digite sua expressão: '))
pilha = []
for paren in exp:
    if paren == '(':
        pilha.append('(')
    elif paren == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')'''
'''exp = str(input('Digite a expressão: '))
pilha = []
cont = 0
for char in exp:
    if char in '()':
        cont += 1
if cont % 2 == 0:
    print('expressão valida')
elif cont % 2 == 1:
    print('expressão inválida')'''