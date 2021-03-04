print('Aprimorando os dicionários do ex093')
'''dados = dict()
gols = list()
jogadores = list()
while True:
    print('-' * 30)
    dados['nome'] = str(input('Nome: '))
    dados['partidas'] = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    for c in range(0, dados['partidas']):
        gols.append(int(input(f"Quantos gols {dados['nome']} fez na partida {c+1}? ")))
    dados['gols'] = gols[:]
    total = sum(gols)
    dados['total'] = total
    jogadores.append(dados.copy())
    gols.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<15}Total')
print('-' * 40)
for pos, jog in enumerate(jogadores):
    print(f"{pos:<4}{str(jog['nome']):<15}{str(jog['gols']):<15}{jog['total']}")
print('-' * 40)
while True:
    info = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if info == 999:
        break
    elif info in range(0, len(jogadores)):
        print(f"LEVANTAMENTO DO JOGADOR {jogadores[info]['nome']}")
        for pos, gol in enumerate(jogadores[info]['gols']):
            print(f"No jogo {pos+1}, {jogadores[info]['nome']} fez {gol} gols")
    else:
        print('\033[91mErro! Parametros inválidos...\033[m')
print('FIM')'''

dados = dict()
partidas = list()
jogadores = list()
while True:
    print('-' * 30)
    dados['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols {dados['nome']} fez na partida {c+1}? ")))
    dados['gols'] = partidas[:]
    total = sum(partidas)
    dados['total'] = total
    jogadores.append(dados.copy())
    partidas.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'Cod ', end='')
for k in dados.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for pos, jog in enumerate(jogadores):
    print(f'{pos:<4}', end='')
    for v in jog.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
while True:
    info = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if info == 999:
        break
    elif info in range(0, len(jogadores)):
        print(f"LEVANTAMENTO DO JOGADOR {jogadores[info]['nome']}")
        for pos, gol in enumerate(jogadores[info]['gols']):
            print(f"No jogo {pos+1}, {jogadores[info]['nome']} fez {gol} gols")
    else:
        print(f'\033[91mErro! Parametros inválidos...\033[mnão existe jogador de código {info}')
print('FIM')
