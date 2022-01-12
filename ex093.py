# Um programa que leia o nome de um jogador de futebol
# e quantas partidas ele jogou. Para cada partida, pedir
# a quantidade de gols feitos por ele. Guardar todas essas
# informações e depois mostrar o total de gols.

jogador = {}

jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['nPartidas'] = int(input('Quantas partidas ele jogou? '))

partidas = []

total = 0
for i in range( jogador['nPartidas'] ):
	nGols = int(input(f'Quantos gols na {i+1}ª partida? '))
	partidas.append( nGols )
	total += nGols

jogador['partidas'] = partidas
jogador['totalGols'] = total

print()
print('\n' + '-' * 40)
print(f"O jogador { jogador['nome'] } fez { jogador['totalGols'] } gols em {jogador['nPartidas']} partidas.")
print('-' * 40)

for i,g in enumerate(jogador['partidas']):
	print(f'  Na partida {i+1}, fez {g} gols.')
