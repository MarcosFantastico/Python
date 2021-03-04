print('Conversor de temperaturas')
tc = float(input('Digite a temperatura em ºC: '))
tk = 273 + tc
tf = tc * 1.8 + 32
print('Temperatura em Kelvin: {:.0f}\nTemperatura em fareinheit: {:.0f}'.format(tk, tf))
