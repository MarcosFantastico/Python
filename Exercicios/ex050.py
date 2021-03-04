from emoji import emojize
print(emojize(':cry: \033[41mSoma de pares!\033[m :smile:', use_aliases=True))
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número inteiro: '))
    if n % 2 == 0:
        s += n
        cont += 1
if cont == 1:
    print('A soma entre o único número par digitado é: {}'.format(s))
else:
    print(f'A soma entre os {cont} números pares digitados é: {s}')
