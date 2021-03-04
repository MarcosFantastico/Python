from random import randint
from time import sleep
print('Palpites para a Mega Sena')
print('-' * 36)
print(f'{"Jogando na Mega Sena":^36}')
print('-' * 36)
qtde = int(input('Digite a quantidade de jogos: '))
jogos = []
nums = []
for c in range(0, qtde):
    while True:
        val = randint(1, 60)
        if val not in nums:
            nums.append(val)
        if len(nums) == 6:
            break
    nums.sort()
    jogos.append(nums[:])
    nums.clear()
print('=+' * 9, f'Seus {qtde} Jogos', '+=' * 9)
for pos, jog in enumerate(jogos):
    print(f'Jogo {pos+1}: {jog}')
    sleep(1)
print('=+' * 9, '<Boa Sorte!>', '+=' * 9)
