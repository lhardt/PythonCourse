# Crie um programa de uma tupla única, com
# nomes e preços. Mostre de forma tabulada
# a listagem de nomes / preços
listagem = (
	'Repolho', 15.50,
	'Alface', 12.08,
	'Tomate', 5.50,
	'Cebola', 9.15
)

print('-' * 25)
print('{:^25}'.format('LISTA DE PREÇOS'))
print('-' * 25)

for iNome, nome in enumerate(listagem[::2]):
	preco = listagem[2*iNome + 1]
	print(f'{nome:.<15} : R${preco:6.2f}')

print('-' * 25)
