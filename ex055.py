# Faça um programa que leia o peso de 5 pessoas,
# e diga qual é o maior e o menor peso.

maior = 0
menor = 0

print('Digite o peso de 7 pessoas:')

for i in range(7):
	peso = int(input('>>>\t'))

	if i == 0 or peso < menor:
		menor = peso
	if i == 0 or peso > maior:
		maior = peso

print('O maior é {} e o menor é {}.'.format(maior, menor))
