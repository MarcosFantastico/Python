print('\033[1;32mBase de conversões!\033[m')
n = int(input('Digite um número inteiro: '))
base = int(input('''Digite:
[ 1 ] Para binário;
[ 2 ] Para octal ou;
[ 3 ] Para hexadecimal: '''))
if base == 1:
    bina = bin(n)
    print('O valor {} convertido para base binária é: {}'.format(n, bina[2:]))
elif base == 2:
    octal = oct(n)
    print('O valor {} convertido para base octal é: {}'.format(n, octal[2:]))
elif base == 3:
    hexa = hex(n)
    print('O valor {} convertido para base hexadecimal é: {}'.format(n, hexa[2:]))
else:
    print('\033[41mErro!. Favor inserir um valor válido...\033[m')
