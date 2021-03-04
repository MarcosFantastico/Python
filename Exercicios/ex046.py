from time import sleep
import emoji
print('\033[91mFogos!\033[m')
sleep(1)
print('O estouro começará em: ')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[1;91mBOOM! :boom::boom: boas festas! :boom::boom:\033[m', use_aliases=True))
