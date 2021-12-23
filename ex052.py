# Faça um programa que leia um inteiro
# e diga se ele é um número primo.

from math import sqrt, floor

numero = int(input('Digite um inteiro positivo, para testar se ele é primo:\n>>>\t'))

limMax = floor(sqrt(numero))

print('Testar até {}'.format(limMax))

isPrimo = (numero > 1)

# Eu sei que há formas mais eficientes (por ex, testo para todo múltiplo de 2)
# e também sei que há uma função pronta para isso.
if isPrimo:
	# Com certeza melhor com while.
	for i in range(2, limMax+1):
		if numero % i == 0:
			isPrimo = False
			break

print('O número é primo? {}.'.format("Sim" if isPrimo else "Não" ))
