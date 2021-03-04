print('\033[96mTriângulos\033[m')
l1 = float(input('Digite o 1º comprimento do triângulo: '))
l2 = float(input('Digite o 2º: '))
l3 = float(input('Digite o 3º: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[32mÉ possível formar um triângulo!\033[m')
    if l1 == l2 == l3:
        print('Um triângulo equilátero! Mais especificamente.')
    elif l1 == l2 != l3 or l3 == l2 != l1 or l1 == l3 != l2:
        print('Um triângulo isósceles! Mais especificamente.')
    else:
        print('Um triângulo escaleno! Mais especificamente.')
else:
    print('\033[31mNão é possível formar um triângulo com essas medidas!\033[m')
