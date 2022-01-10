# O usuário digita 7 valores numéricos
# que ficam em uma lista-de-duas-listas única,
# separada por pares e ímpares. Mostre os
# conjuntos separadamente, de forma crescente

numeros = []
pares = []
impares = []

# Shallow
numeros.append(pares)
numeros.append(impares)

print('Digite 7 números')

for i in range(7):
	try:
		num = int(input('>>> '))

		if num % 2 == 0:
			pares.append(num)
		else:
			impares.append(num)

	except Exception as e:
		print(f'Opa! {e}. ')

pares.sort()
impares.sort()

print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')
