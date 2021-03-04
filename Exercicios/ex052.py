'''print('Primos!')
n = int(input('Digite um número inteiro: '))
print('O número que você digitou é: ', end='')
multiplo = 0
res = ''
for c in range(2, n):
    if n % c == 0:
        multiplo += 1
if multiplo == 0:
    res = 'Primo'
else:
    res = 'Não primo'
print(res)'''

print('Primos!')
cores = {"verdebold": '\033[1;92m',
         "vermbold": '\033[1;91m',
         "limp": '\033[m',
         "amrlobold": '\033[1;93m'}
n = int(input('Digite um número inteiro: '))
print('Os divisores do número que você digitou são: ', end='\n')
divisores = 0
for c in range(1, n+1):
    if n % c == 0:
        divisores += 1
        print(f'{cores["verdebold"]}', end='')
    else:
        print(f'{cores["vermbold"]}', end='')
    print(f'{c}{cores["limp"]}', end=' ')
if divisores == 2:
    print(f'\nO número digitado tem somente {cores["amrlobold"]}{divisores}{cores["limp"]}'
          f' divisores, logo: \033[1;97;42mÉ PRIMO\033[m')
else:
    print(f'\nO número digitado tem {cores["amrlobold"]}{divisores}{cores["limp"]} divisores, logo:'
          f' \033[1;97;41mNÃO é PRIMO\033[m')
