import emoji
msg = 'Olá Mundo'
print(emoji.emojize('{} {}:thought_balloon: :eyes:{}!'.format(msg, '\033[91m', '\033[m'), use_aliases=True))
