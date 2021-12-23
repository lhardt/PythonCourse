# Calcule a soma de todos os números
# ímpares múltiplos de 3 entre 1 e 500

soma = 0

for i in range(3,501, 6):
	soma += i
	print('{}'.format(i), end=' ')


print('\nA soma é {}'.format(soma))
