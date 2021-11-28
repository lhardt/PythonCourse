# Crie um programa em python que abra e
# toque um arquivo MP3.

from playsound import playsound

filename = input('Digite o nome do arquivo:\n>>>\t')

try:
    file = open(filename, 'r')
    file.close()
    playsound(filename)
except IOError:
    print('O arquivo não existe!')
