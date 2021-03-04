print('Multas!')
km = float(input('\033[34mDigite a velocidade do seu carro: \033[m'))
if km > 80:
    print('\033[31mVoçê foi multado por ultrapassar a velocidade máxima permitida de 80km/h!\033[m')
    preco = (km - 80) * 7
    print('O preço da sua multa é : {}R${:.2f}{}'.format('\033[33m', preco, '\033[m'))
else:
    print('\033[30;42mVocê não foi multado!\033[m\n')
print('\033[4;30;44mAnde sempre com segurança!\033[m')
