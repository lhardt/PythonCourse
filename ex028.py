# Condição resumida:
# printf('Oi' if (true) else 'Tchau')

# Escreva um programa que faça o computador "pensar"
# em um núm inteiro de 0 a 5 e peça para o usuário descobrir
# qual é o número. O programa deve escrever na tela se o usuário
# acertou.
from random import random

numero = int(random() * 6)

input = str(input("Adivinhe meu número entre 0 e 5\n>>>\t")).strip()

if input.isnumeric() :
	acertou = (numero == int(input))
	if acertou:
		print( "Acertou!\n")
	else:
		print("Não foi desta vez... Pensei em {}\n".format(numero))
else:
	print("Não digitou um número!!")
