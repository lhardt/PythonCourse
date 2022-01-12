# Um programa em que 4 jogadores jogam um dado
# e tenham resultados aleatórios. Guarde esses
# valores em um dicionáio, sabendo que quem
# ganhou tirou o maior valor. Não leia nomes,
# só dê um "ranking"
from random import randint

dados = {
	'jogador1' : randint(1,6),
	'jogador2' : randint(1,6),
	'jogador3' : randint(1,6),
	'jogador4' : randint(1,6),
}

for k,v in dados.items():
	print(f'{k} fez {v} pontos!')

print()
print('-'*30)
print('{:^30}'.format('PÓDIO'))
print('-'*30)

# Cópia. Preservamos os dados originais.
items = list(dados.items())

# Quatro iterações de escolher o maior, printar e remover.
for iter in range(4):
	maxI = 0

	# Procurando o maior e salvando o índice.
	for iPlayer in range(1, 4-iter):
		if items[maxI][1] < items[iPlayer][1]:
			maxI = iPlayer

	print(f' {iter+1}º:   {items[maxI][0]} com {items[maxI][1]} pontos.')

	items.pop(maxI)

print('-'*30)
