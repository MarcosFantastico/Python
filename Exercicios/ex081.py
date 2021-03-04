print('Vários números!')
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(lista)
print(f'Foram gerados {len(lista)} números: ')
print('Lista de forma decrescente: ')
lista.sort(reverse=True)
print(lista)
if 5 not in lista:
    print('O número 5 \033[91mNÃO\033[m está na lista!')
else:
    print('O número 5 \033[1;92maparece\033[m na lista!')
