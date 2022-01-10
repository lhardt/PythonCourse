# Leia nome e peso de várias pessoas, em uma lista composta só
# Diga:
#  1) quantas pessoas foram cadastradas
#  2) a lista das pessoas que têm o maior peso
#  3) a lista das pessoas que têm o menor peso

pessoas = []

maiorPeso = 0
menorPeso = 0

print("PARA PARAR, DEIXE EM BRANCO!\n-------")

while True:
	try:
		pessoa = [ ]
		print(f"Digite o nome e o peso da {len(pessoas)+1}ª pessoa")
		pessoa.append( input('>>> ') )

		if pessoa[0] == '':
			print('Nome vazio. saindo')
			break

		pessoa.append( int(input('>>> ')) )

		pessoas.append(pessoa)

		if len(pessoas) == 1:
			maiorPeso = menorPeso = pessoa[1]
		if pessoa[1] > maiorPeso :
			maiorPeso = pessoa[1]
		elif pessoa[1] < menorPeso:
			menorPeso = pessoa[1]

	except Exception as e:
		print(f'Erro! Saindo do cadastro. {e}')

print(f'Foram inseridas as {len(pessoas)} pessoas!')

print('Quem tem o maior peso: ', end='')

for pessoa in pessoas:
	if pessoa[1] == maiorPeso:
		print(f'"{pessoa[0]}"', end=' ')

print('\nQuem tem o menor peso: ', end='')

for pessoa in pessoas:
	if pessoa[1] == menorPeso:
		print(f'"{pessoa[0]}"', end=' ')
