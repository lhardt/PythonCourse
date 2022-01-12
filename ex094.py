# Nome sexo e idade de várias pessoas.
# a) Quantas pessoas foram cadastradas.
# b) A média de idade do grupo.
# c) A lista de todas as mulheres.
# d) A lista de todas as pessoas com idade acima da média.

def lerPessoa():
	pessoa = {}
	pessoa['nome'] = str(input('Nome: '))
	pessoa['idade'] = int(input('Idade: '))
	sexoStr = str(input('Sexo [M/F]: ')).strip().upper()

	if sexoStr != 'M' and sexoStr != 'F':
		raise Exception('Sexo Inválido!')

	pessoa['sexo'] = sexoStr

	return pessoa

pessoas = []

somaIdade = 0

while True:
	try:
		print()
		novaPessoa = lerPessoa()
		pessoas.append(novaPessoa)

		somaIdade += novaPessoa['idade']
	except Exception as e:
		print(f'Saindo... {e}')
		break


print()



if len(pessoas) > 0:
	mediaIdade = somaIdade / len(pessoas)

	print(f'O grupo tem { len(pessoas) } pessoas')
	print(f'A média de idade do grupo é { mediaIdade } anos')

	print('As mulheres cadastradas são: ', end='')
	for it in pessoas:
		if it['sexo'] == 'F':
			print(it['nome'], end=' ')

	print('\nAs pessoas que têm idade acima da média são: ', end='')
	for it in pessoas:
		if it['idade'] >= mediaIdade:
			print(it['nome'], end=' ')
