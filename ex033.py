# Faça um programa que leia 3 números e mostre o maior e o menor.

numbers = []

for i in range(3) :
	numbers.append( int( input('Digite o  {}º número.\n>>>\t'.format(i+1)) ) )

numbers.sort()

print('O maior é: {} e o menor é {}'.format(numbers[2], numbers[0]))
