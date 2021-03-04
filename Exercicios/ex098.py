from time import sleep


def contador(i, f, p):
    if i < f:
        if p > 0:
            print(f'Contagem de {i} a {f} de {p} em {p}')
            for c in range(i, f + 1, p):
                print(f'{c} ', end='')
                sleep(0.25)
            print()
        elif p < 0 or p == 0:
            p = 1
            print(f'Contagem de {i} a {f} de {p} em {p}')
            for c in range(i, f + 1, p):
                print(f'{c} ', end='')
                sleep(0.25)
            print()
    elif i > f:
        if p < 0:
            print(f'Contagem de {i} a {f} de {p * -1} em {p * -1}')
            for c in range(i, f - 1, p):
                print(f'{c} ', end='')
                sleep(0.25)
            print()
        elif p > 0:
            print(f'Contagem de {i} a {f} de {p} em {p}')
            for c in range(i, f - 1, -p):
                print(f'{c} ', end='')
                sleep(0.25)
            print()
        elif p == 0:
            p = 1
            print(f'Contagem de {i} a {f} de {p} em {p}')
            for c in range(i, f - 1, -p):
                print(f'{c} ', end='')
                sleep(0.25)
            print()


def linha():
    print('-' * 25)


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora personalize a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
linha()
contador(ini, fim, pas)
print(f'Fim!')

'''from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} a {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            # O parâmetro flush serve para remover o buffer do sleep ou seja o codigo não sera executado depois de
            # todas as contagens do sleep
            print(f'{cont} ', end='', flush=True)
            sleep(0.4)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.4)
            cont -= p
        print('Fim!')


def linha():
    print('-' * 25)


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora personalize a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
linha()
contador(ini, fim, pas)'''
