cores = {'vermelho': '\033[31m', 'verde': '\033[32m', 'rosa': '\033[35m', 'limpa': '\033[m'}
print('{}Primeiro{} e {}Último{} nome'.format(cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa']))
nome = str(input('Digite seu nome: ')).strip()
lista = nome.split(' ')
prmr = lista[0]
ltm = lista[len(lista) - 1]
print('O nome {}{}{} tem:\nPrimeiro nome: {}{}{}\nÚltimo nome: {}{}{}'
      .format(cores['rosa'], nome, cores['limpa'], cores['verde'], prmr, cores['limpa'], cores['vermelho'], ltm,
              cores['limpa']))
