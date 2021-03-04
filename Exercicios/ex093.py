from emoji import emojize
print('Cadastro de Jogadoe de Futebol')
jogador = dict()
jogador['nome'] = str(input('Nome: '))
partidas = int(input('Quantidade de partidas jogadas: '))
arraygols = []
total = 0
for c in range(0, partidas):
    gols = int(input('Quantos gols na partida {}? '.format(c+1)))
    total += gols
    arraygols.append(gols)
jogador['gols'] = arraygols[:]
jogador['total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-=' * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas: ")
for pos, gol in enumerate(arraygols):
    print(emojize(f":arrow_right: Na partida {pos + 1}, {jogador['nome']} fez {gol} gols!", use_aliases=True))
print(emojize(f':arrow_right: Total de {total} gols!', use_aliases=True))
