from datetime import date
from emoji import emojize
print(emojize('Maioridade!:underage:', use_aliases=True))
atual = date.today().year
contadormaior = 0
contadormenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        contadormaior += 1
    else:
        contadormenor += 1
print(f'Pessoas menores de idade: \033[1;31m{contadormenor}\033[m\nPessoas maiores de idade: '
      f'\033[32m{contadormaior}\033[m')
