# Crie uma matriz 3x3 e a preencha pelo
# teclado. Imprima toda a matriz, com a
# formatação correta. (linha-depois-coluna)
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
