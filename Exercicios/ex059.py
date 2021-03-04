from time import sleep
from emoji import emojize
print(emojize(':arrow_right: Operando valores! :arrow_left:', use_aliases=True))
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
maior = n1
escolha = 0
quebra = '+=' * 12
while escolha != 5:
    escolha = int(input('''Escolha uma opção:
[ 1 ] Somar;
[ 2 ] Multiplicar;
[ 3 ] Maior;
[ 4 ] Novos números;
[ 5 ] Sair: '''))
    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é: {n1 + n2}')
        print(quebra)
    elif escolha == 2:
        print(f'O produto entre {n1} e {n2} é: {n1 * n2}')
        print(quebra)
    elif escolha == 3:
        if n2 > maior:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é: {maior}')
        print(quebra)
    elif escolha == 4:
        n1 = int(input('Digite o número novo: '))
        n2 = int(input('Digite o segundo número novo: '))
        print(quebra)
    else:
        while escolha not in range(1, 6):
            escolha = int(input('\033[91mErro!\033[m Digite um parametro válido! '))
print('Finalizando...')
sleep(1)
print('Fim! Volte sempre!')
