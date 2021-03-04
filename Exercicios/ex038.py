print('\033[95mComparador\033[m')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
if n1 > n2:
    print('O \033[92mprimeiro valor {} \033[mé maior'.format(n1))
elif n2 > n1:
    print('O \033[92msegundo valor {} \033[mé maior'.format(n2))
else:
    print('\033[91mNão existe maior!\033[m Ambos valores são \033[93mIGUAIS!\033[m')
