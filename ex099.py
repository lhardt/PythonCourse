# Crie uma função chamada maior, que imprima o maior valor de uma lista.

def maior(lista):
	length = len(lista)

	if length == 0:
		print('A lista não tem elementos. Não há maior número')
	else:
		print(f'A lista informada tem {length} elementos e o maior é {max(lista)}')


maior([1,2,3,4,99,5])
