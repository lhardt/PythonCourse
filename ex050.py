# Um programa que leia 6 inteiros e mostre
# a soma dos que forem pares.
N_NUMEROS = 6

numeros = []
somaPares = 0

print('Digite {} números inteiros.'.format(N_NUMEROS))

for i in range(N_NUMEROS):
	numeros.append(int(input('>>>\t')))

	if numeros[i] % 2 == 0:
		somaPares += numeros[i]

print('A lista de números é {} e a soma dos pares é {}'.format(numeros, somaPares))
