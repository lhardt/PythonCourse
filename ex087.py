# Aprimorando o desafio anterior, mostre:
# a) A soma de todos os pares digitados,
# b) A soma de toda a 3ª coluna
# c) o maior valor da 2ª linha

def exercicioAnterior():
	print('Digite uma matriz:')

	matriz = []

	for i in range(3):
		linha = []
		print(f'{i+1}ª linha:')
		for j in range(3):
			linha.append( int(input('>>> ')) )

		matriz.append(linha)


	for i in range(3):
		print('[', end='')

		for j in range(3):
			print(f' [{matriz[i][j]:^3}] ', end='')


		print(']')

	return matriz


matriz = exercicioAnterior()

sPares = 0
s3a = 0
maior2a = max(matriz[1])

for i in range(3):
	for j in range(3):
		if matriz[i][j] % 2 == 0:
			sPares += matriz[i][j]

		if i == 2:
			s3a += matriz[i][j]


print(f'A soma dos pares é {sPares}')
print(f'A soma da 3ª linha é {s3a}')
print(f'O maior número da 2ª linha é {maior2a}')
