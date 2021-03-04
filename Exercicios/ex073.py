print('CBF')
times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio', 'Corinthians',
         'Bragantino', 'Athletico-PR', 'Santos', 'Ceará SC', 'Atlético-GO', 'Sport Recife', 'Fortaleza',
         'Vasco da Gama', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')
for t in times:
    print(t)

print('Os 5 primeiros colocados:')
print(times[0:5])
print('Os 4 últimos colocados:')
# print(times[16:20])
print(times[-4:])
print('Ordem alfabética:')
print(sorted(times))
print('O Atlético MG está na {}ª posição'.format(times.index('Atlético-MG')+1))

'''print('CBF')
times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio', 'Corinthians',
         'Bragantino', 'Athletico-PR', 'Santos', 'Ceará SC', 'Atlético-GO', 'Sport Recife', 'Fortaleza',
         'Vasco da Gama', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')
print('A) Os 5 primeiros colocados são:')
for c in range(0, 5):
    print(f'{c + 1} - {times[c]}')
print('B) Os últimos 4 colocados da tabela são:')
for c in range(15, 20):
    print(f'{c+1} - {times[c]}')
print(f'C) Lista em ordem alfabética:\n{sorted(times)}')
print(f'D) O time Vasco da Gama está na {times.index("Vasco da Gama")+1}ª posição:')'''
