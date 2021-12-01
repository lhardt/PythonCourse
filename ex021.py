# Crie um programa em python que abra e
# toque um arquivo MP3.

import pygame



filename = input('Digite o nome do arquivo:\n>>>\t')

try:
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play(-1)
	pygame.event.wait()
	input("Pressione ENTER para sair. ")
except IOError:
    print('O arquivo não existe!')
