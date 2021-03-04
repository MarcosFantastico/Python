from random import randint
from time import sleep
from operator import itemgetter # modulo usado para definir o critério de ordenação
print('Jogo de dados em python')
jogadores = dict()
print('Valores sorteados:')
for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou: {v}')
    sleep(1)
print('='*10 + ' Ranking ' + '='*10)
ranking = sorted(jogadores.items(), reverse=True, key=itemgetter(1))#1 especifica ordenação pelo valor e 0 pelas keys
for pos, val in enumerate(ranking):
    print(f'    {pos+1}º Lugar: {val[0]} com {val[1]}')
    sleep(1)
