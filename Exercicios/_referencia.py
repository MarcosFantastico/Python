# mostrando o tipo da variável
s = 'ola'
print(type(s))

# tipos primitivos
inteiro = int(input('Digite um número inteiro'))
VF = bool(input('Digite um algo para verdadeiro e nada para falso'))
real = float(input('Digite um número real'))
string = str(input('Digite uma letra ou character'))

# ordem de precedência de operadores aritméticos
# 1 ()
# 2 **
# 3 * / // %  -> // operador para uma divisão inteira
# 4 + -
# 81**(1/x) ou pow(81,1/x) -> raiz

# métodos para objetos string
# ex004

#print
# formatando string
nome = input('Digite seu nome: ')
print('Prazer em conhece-lo(a) {:=^20}'.format(nome))
# formatando numeros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um: '))
d = n1/n2
print('A divisão entre os valores é igual a {:.3f}'.format(d))
# pré-alocando espaços
n = 2
print('{:2}'.format(n))
# É possivel replicar strings utilizando o operador *
print('-' * 10)
# \n quebra a linha do print
# end = ' ' junta 2 prints escritos separadamente

#Modulos
# Importando todos os dados de uma biblioteca
import math
num = int(input('Digite um número '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
# Importando um dado específico de uma biblioteca
from math import sqrt, floor
num = int(input('Digite um número'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
# Gerando números aleatórios entre 0 e 1 e entre um intervalo especificado
import random
num = random.random()
numint = random.randint(1, 20)
print(num, numint)
# Baixando e utilizando bibliotecas de Módulos da internet
import emoji
print(emoji.emojize('Olá, Mundo :earth_americas:!', use_aliases=True))

# aula 09
#Fatiamento de string
# Escolhendo caracter
frase = 'Marcos'
print(frase[0])
# Escolhendo cadeia de caracteres
print(frase[0:2])
# Pulando por intervalos
print(frase[0:5:2])
print(frase[0::2])
# Especificando inicio
print(frase[1:])
# Especificando fim
print(frase[:1])
# Comprimento da frase
len(frase)
# Contando letras; Especificando intervalo para contagem
frase.count('o')
frase.count('o', 0, 4)
# Encontrando partes de uma frase
frase.find('os')
# Se existe ou não
print('arcos' in frase)
# Transformação
frase.replace('Marcos', 'Android')
frase.upper()
frase.lower()
frase.capitalize() # Somente a primeira letra fica maiúscula
frase.title() # Primeira letra de cada palavra fica maiúscula
# Removendo espaços no inicio e no final da string; Espaços da direita; Espaços da esquerda
frase = '   Marcão    '
frase.strip()
frase.rstrip()
frase.lstrip()
# Divisão
frase = 'Marcos Vinícius de Lima e Chagas'
frase.split() # separa a string em uma lista de strings
# Junção
'-'.join(frase)

# aula 10
# Estrutura de condição simples
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número é par!')
print('Tenha um bom dia')
# Estrutura de condição composta
tempo = int(input('qtos anos vc tem? '))
if tempo <= 3:
    print('voce é novo')
else:
    print('você é velho')
# Ou (condição simplificada)
print('voce é novo' if tempo <= 3 else 'voce é velho')

# aula 11
# Cor em pythom ANSI
'\033[style;text;bakgroundm'
'style -> 0 = none; 1 = bold; 4 = underline; 7 = negative'
'text -> de 30 a 37'
'back -> 40 a 47'

# aula 12
# condições aninhadas (umas dentro de outras)
nome = str(input('Digite seu nome: '))
if nome == 'Marcos':
    print('Que belo nome!')
elif nome == 'Lucas' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'João Pedro Paulo José':
    print('Seu nome é normal!')
else:
    print('Seu nome é diferente!')
print('Tenha um bom dia, {}!'.format(nome))

# aula 13 estrutura de repetição for
for c in range(1, 3):
    print(c)
print('fim')

for c in range(6, 0, -1):
    print(c)
print('fim')

for c in range(1, 8, 2):
    print(c)

n = int(input('Digite um número: '))
for c in range(1, n + 1):
    print(c)
print('Fim')

i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f + 1, p):
    print(c)
print('fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um numero: '))
    s += n
print(f'A soma é: {s}')

# aula 14 estrutura de repetiçao while ( usada quando não se sabe o fim ) por isso há o uso do teste lógico
# While como for
c = 1
while c < 10:
    print(c)
    c += 1
print('fim')

for c in range(1, 10):
    print(c)
print('fim')

# uso do while sem especificar o final
# ex: 1
n = 1
while n != 0: # flag -> condição de parada
    n = int(input('Digite um valor, digite 0 para parar: '))
print('fim')
# ex: 2
n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print('Fim')
# ex: 3
n = 1
cont_par = cont_impar = 0
while n != 0:
    n = int(input('Digite um número, digite 0 para parar: '))
    if n % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print('voce informou {} numeros pares e {} numeros impares'.format(cont_par, cont_impar))

# aula 15 interrompendo repetição while com break
# loop infinito
cont = 1
while True:
    print(cont, ' -> ', end='')
# Uso do break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}') # -> interpolaçao
# Mundo 3
# é possivel iniciar a variavel com (), {}, [], ou somente , entre os elementos

# aula 16 - Tuplas ()
# As tuplas () são imutáveis no python ou seja não é possivel trocar, adicionar ou retirar elementos específicos de uma
# tupla por um comando decorrente do programa
# ITEMS são iniciados com ():
# variável simples (guarda 1 variavel)
lanche = 'x'
# variavel composta ( guarda mais de 1 variavel )
lanches = ('hamburguer', 'suco', 'pizza', 'pudim')
# contando da direita para a esquerda
print(lanches[-1])
print(lanches[-2])
print(lanches[-3])
print(lanches[-4])
# formas simplificadas do conceito acima (fatiamentos)
print(lanches[-1::-1])
print(lanches[-1:-5:-1])
# usando o for para exibir os elementos do array
for c in lanches:
    print(c)
# usando o for para exibir itens
for c in range(0, len(lanches)):
    print(f'Comi: {lanches[c]}')
print('Comi muito')

for c in lanches:
    print(f'Eu vou comer {c}')
print('Comi pra caramba!')
# exibindo o item e a posição usando o 2 exemplo dado anteriormente:
for pos, comida in enumerate(lanches):
    print(f'eu comerei {comida} na posição {pos}')
# exibindo os items em ordem:
print(sorted(lanches))
# concatenando tuplas:
a = (1, 5, 2, 4)
b = (6, 8, 5)
c = a + b
print(c)
print(len(c))
# conta a quantidade de vezes de um valor
print(c.count(5))
# mostra o índice
print(c.index(5))
# Deslocamento
print(c.index(5, 2))
# É possivel ter elementos de tipos diferentes em uma mesma tupla
pessoa = ('marcos', 'm', 17, 49.5)
# É possivel apagar uma variavel em contrapartida muda-la não é possivel
del(pessoa)
print(pessoa)

# Aula 17 - Listas []
# As listas são iniciadas com [] ou lista = list() e SÃO MUTÁVEIS, ou seja e possivel alterar, adicionar e retirar um
# elemento com um comando ao decorrer do programa
# Adicionando elementos à lista (no final) e substituindo elementos por outros:
nums = [1, 2, 3]
nums.append(4)
num[0] = 9
num[1] = 10
# Adicionando elementos à lista (posição específica):
comida = ['suco', 'hanmburguer', 'file', 'salsicha']
comida.insert(0, 'cachorro quente')
comida.insert(2, 'geleia')
# Apagando elemento especificando sua posição utilizando o COMANDO del:
# Nota: qualquer eliminação feita nas listas reposiciona e organiza a contagem dos índices automaticamente
objetos = ['cadeira', 'lapis', 'mouse', 'teclado']
del objetos[3]
# Ou pode-se utilizar o MÉTODO pop(). obs(normalmente é utilizado para apagar ultimo elemento mas é possivel especificar
# o índice)
personagens = ['Naruto', 'Sasuke', 'Sakura', 'Kakashi']
personagens.pop(1)
# Apaga o ultimo elemento
personagens.pop()
# Apagando elementos usando seu valor como parâmetro utilizando o METODO REMOVE():
shingeki = ['Armin', 'Eren', 'Mikasa', 'Anne']
shingeki.remove('Armin')
# Apagando com condição
death = ['Light', 'Misamisa', 'Mikami', 'Near']
if 'Light' in death:
    death.remove('Light')
# Nota: O METODO remove caso haja 2 ocorrencias do valor desejado a ser apagado ele elimina a 1ª ocorrencia da direita
# para esquerda:
vals = [1, 4, 2, 3, 2, 5]
# Criando listas utilizando o range pelo metodo list()
valores = list(range(4, 11))
# Criando lista desordenada e ordenando-a com o METODO sort():
# Nota: após a mudança de posição não é possivel reverte-la novamente
nume = [4, 7, 5, 1, 2, 8, 9]
nume.sort()
# Ordenando em ordem decrescente utilizando o METODO sort() e o PARAMETRO reverse :
nume.sort(reverse=True)

# Ex1:
valoreis = list()
valoreis.append(4)
valoreis.append(5)
valoreis.append(6)
print('Os valores são: ', end='')
for v in valoreis:
    print(v, end=' ')

# Ex2:
numeros = list()
for c in range(1, 6):
    numeros.append(int(input(f'Digite o {c}º valor: ')))

for pos, nums in enumerate(numeros):
    print(f'Na posição {pos}, encontrei o valor: {nums}')

# Ex3:
# Nota: ao igualar 2 listas o python cria uma ligação entre elas e altera os dados em ambas!
a = [1, 2, 4, 6]
b = a
b[2] = 20
print(f'''Lista A: {a}
Lista B: {b}''')

# Ex4: Resolvendo o problema criado anteriormente utilizando fatiamento para a produção de uma cópia:
a = [1, 2, 4, 6]
b = a[:]
b[2] = 20
print(f'''Lista A: {a}
Lista B: {b}''')

# Aula 18 Listas parte 2 Listas compostas
# É possível dar appends de estruturas
# Obs o indice 0 de pessoas recebera todos os valores de dados
dados = ['pedro', 20]
pessoas = list()
pessoas.append(dados[:])
# É possivel também declarar da seguinte forma: (3 listas em uma)
pessoas = [['pedro', 25], ['maria', 30], ['josé', 10]]
# manipulando dados específicos
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
# printando pessoas:
for i in pessoas:
    print(i)
# printando nomes e idades separadamente:
for i in pessoas:
    print(i[0])
for i in pessoas:
    print(i[1])
# nomes e idade com texto
for i in pessoas:
    print(f'{i[0]} tem {i[1]} anos de idade')
# usuario preenchendo nome e idade:
galera = list()
dado = list()
for pes in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
# Printando com condição:
galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for i in galera:
    if i[1] > 19:
        print(f'{i[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{i[0]} é menor de idade')
        totmenor += 1
print(f'Temos no total {totmaior} maiores e {totmenor} menores de idade!')
# Aula 19 - Dicionários
# os dicionários são iniciados com {} são semelhantes as tuplas e as listas mas podem possuir índices literais
# Declarando um dicionário:
dados = dict()
dadoss = {}
# Declarando com dados inbutidos:
pess = {'nome': 'Pedro', 'idade': 25}
print(f'O {pess["nome"]} tem {pess["idade"]}')
# Dando appends com índice e elemento declarados
dados['sexo'] = 'M'
# Removendo Elementos com o índice
del(pess['sexo'])
del(pess['nome'], pess['idade'])
# Printando valores do dicionário:
print(dados.values())
# Indices ou chaves
print(dados.keys())
# valores e chaves
print(dados.items())
# for com keys e values
# nas listas e nas tuplas usa-se o comando enumerate nos dicionários é utilizado o método items()
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
for k, v in pess.items():
    print(f'O {k} é: {v}')
# tuplas com dicionários:
locadora = ({'titulo': 'Star wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'})
# listas com dicionários:
brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
# para fazer copias de dicionários diferentemente das listas a qual usa-se [:], utiliza-se o metodo copy
# ex:
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
for estad in brasil:
    for v in estad.values():
        print(f'{v}', end=' ')
    print()
# Uso do método itemgetter para ordenar um dicionário:
from operator import itemgetter
from random import randint
nums = {[randint(0, 10)]*10}
# ordenando por indice (0) e por valores (1)
ordemi = sorted(nums, key=itemgetter(0))
ordemv = sorted(nums, key=itemgetter(0))
# Aula 20 - Funções(parte 1)
# declarando uma função para mostrar linhas
def mostralinha():
    print('-'*40)


# Programa principal
mostralinha()
print('Aprenda python')
mostralinha()
print('Marcão brabo')
mostralinha()
# declarando função para exibir linhas usando um parâmetro
def mensagem(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)
mensagem('Sistema de Alunos')
# função para somar 2 valores
def soma(a, b):
    print(f'A = {a} B = {b}')
    sum = a + b
    print(f'A soma entre {a} e {b} é {sum}')
soma(a=int(input('Valor 1:')), b=int(input('Valor 2: ')))
# função que recebe múltiplos parametros (empacotamento de parametros)
def soman(*num):# * recebe a função de desempacotar
    print(f'Valores: {num}')
    soma = sum(num)
    print(f'A soma é {soma}')
# função com estrutura de repetição
def mul(*var):
    cont = len(var)
    for c in var:
        print(f'{var} ', end='')
        print(f'Ao todo são {cont} valores')
    print()
mul(2, 3, 4, 1)
# função que dobra valores de um array
def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont += 1
valores = [2, 4, 6 ,7]
dobra(valores)

# Uso do parametro flush e explicação: ex098

