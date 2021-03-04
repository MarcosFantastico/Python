import emoji
print(emoji.emojize(':1234:Tabuada!:1234:', use_aliases=True))
n = int(input('Digite o número para o cálculo da tabuada: '))
for c in range(0, 11):
    print(f'{c:2} X \033[92m{n} = {c * n}\033[m')
