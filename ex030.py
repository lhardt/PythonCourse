# Crie um programa que leia um número inteiro na tela,
# e diga se ele é par ou ímpar.

num	= int(input('Digite um número inteiro:\n>>>\t'))

print('O número é {}.\n'.format(
	"par" if (num % 2 == 0) else "ímpar"
))
