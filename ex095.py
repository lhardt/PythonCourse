# Faça o exercício 93, mas com múltiplos jogadores.

def lerJogador():
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

	return jogador

def printJogador(jogador):
	print('\n' + '-' * 40)
	print(f"O jogador { jogador['nome'] } fez { jogador['totalGols'] } gols em {jogador['nPartidas']} partidas.")
	print('-' * 40)

	for i,g in enumerate(jogador['partidas']):
		print(f'  Na partida {i+1}, fez {g} gols.')


jogadores = []

while True:
	try:
		print('-'*10)
		jogadores.append( lerJogador() )
	except ValueError as e:
		break

print('-' * 40)

print(f" ID\t{'Nome':15} NPart  TotalGols")
for i,j in enumerate(jogadores):
	print(f" {i}\t{j['nome']:15} {j['nPartidas']}\t{j['totalGols']}")

while True:
	id = int(input('\nDigite o ID de qual você quer saber:\n>>>\t'))

	if id < len(jogadores):
		printJogador(jogadores[id])

	else:
		break
