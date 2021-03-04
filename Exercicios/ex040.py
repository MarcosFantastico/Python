print('\033[1;36mNotas!\033[m')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a média é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('Média abaixo de 5! {}Reprovado!{}'.format('\033[1;31m', '\033[m'))
elif 5 <= media < 7:
    print('Média entre 5 e 6.9! {}Recuperação!{}'.format('\033[4;33m', '\033[m'))
else:
    print('Média 7 ou superior! {}Aprovado!{}'.format('\033[1;32m', '\033[m'))
