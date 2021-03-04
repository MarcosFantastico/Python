import pygame
print('Abrindo um arquivo mp3')
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Pressione enter para parar... ')
