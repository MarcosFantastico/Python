print('Nome SILVA')
nome = str(input('Digite seu nome: ')).strip()
silva = "silva" in nome.lower()
if not silva:
    print('{} tem "SILVA" no nome? \033[31m{}\033[m!'.format(nome, silva))
else:
    print('{} tem "SILVA" no nome? {}{}{}!'.format(nome, '\033[32m', silva, '\033[m'))
