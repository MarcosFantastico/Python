from time import sleep


def linha():
    print('-='*20)


def maior(*mul):
    print('Analisando os valores passados...')
    maximum = 0
    qtde = len(mul)
    for pos, val in enumerate(mul):
        print(f'{val} ', end='')
        sleep(0.4)
        if pos == 0:
            maximum = val
        elif val > maximum:
            maximum = val
    print()
    print(f'Foram analisados {qtde} números ao todo!')
    sleep(0.4)
    print(f'O maior valor analisado foi {maximum}')
    linha()


linha()
print('Analisador de números!')
linha()
maior(2, 3, 4, 5, 1)
maior()
maior(435, 546, 123, 654, 274, 864, 834)
maior(9, 6, 7, 67, 53, 2, 45, 76, 4)
