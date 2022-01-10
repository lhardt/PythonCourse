# Faça um programa que leia 5 valores
# e os guarde em uma lista.
# No final, mostre qual o maior e o menor
# valores digitados e suas respectivas
# posições

print('Digite 5 números inteiros:')

try:
	lista = [ ]
	for i in range(5):
		lista.append( input('>>>\t'))

	maiorValor = max(lista)
	print(f'\nO maior valor foi { maiorValor } nas posições: ', end='')

	for i, item in enumerate(lista):
		if item == maiorValor:
			print(f'{i+1}ª', end=' ')

	menorValor = min(lista)
	print(f'\nO maior valor foi { menorValor } nas posições: ', end='')

	for i, item in enumerate(lista):
		if item == menorValor:
			print(f'{i+1}ª', end=' ')


except Exception as e:
	print(f'Erro... {e}')
