# Crie um programa que leia nome e preço de produtos.
# O programa pergunta sempre se o usuário quer continuar,
# e ao final mostra:
# a) Qual é o total gasto
# b) Quantos produtos custam mais de 1000
# c) O nome do produto mais barato.

def wantsToLeave():
	result = ''
	while not result in ['S', 'N']:
		result = input('Deseja sair? [S/N]\n>>>\t').strip().upper()

	return result == 'S'

total = 0
nProdutosCaros = 0
precoMaisBarato = -1
nomeMaisBarato = 0

notExit = True

while notExit:
	try:
		nome = input('Nome do produto: ').strip()
		preco = float(input('Preço do produt: ').strip())

		total += preco
		nProdutosCaros += 1 if preco >= 1000 else 0

		if preco < precoMaisBarato or precoMaisBarato == -1:
			nomeMaisBarato = nome
			precoMaisBarato = preco

	except Exception as e:
		print(f'Erro: {e}')

	notExit = not wantsToLeave()

print('------------------')
print(f'Valor total: R$ {total:.2f}')
print(f'# Produtos acima de 1000.00: {nProdutosCaros}')
print(f'Produto mais barato: {nomeMaisBarato} ({precoMaisBarato})')
