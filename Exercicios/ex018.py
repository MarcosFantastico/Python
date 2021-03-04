import math
print('Seno, cosseno e tangente')
angulo = float(input('Digite o valor do ângulo para calcular seu seno, cosseno e tangente: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo {}, tem:\nSeno = {:.4f};\nCosseno = {:.4f};\nTangente = {:.4f}'.format(angulo, sen, cos, tan))
