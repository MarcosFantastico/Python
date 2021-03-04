from emoji import emojize
print(emojize('Soma de ímpares multiplos de :three: entre 1_500', use_aliases=True))
s = 0
valores = 0
print('Os ímpares múltiplos de 3 são:')
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        valores += 1
'''for c in range(3, 501, 3):
    if c % 2 != 0:
        s += c
        valores += 1'''
print(f'A soma entre todos os \033[91m{valores}\033[m valores é: \033[1;92m{s}\033[m')
