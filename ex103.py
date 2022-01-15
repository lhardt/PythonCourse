# Crie a função ficha com doi parametros opcionais.
# Nome do jogador e quantos gols ele marcou,
# mesmo que um dado não tenha sido preenchido.

def ficha(nome='<desconhecido>', nGols=0):
	print(f'O jogador {nome} fez {nGols} gols no campeonato')


nome = input('Digite o nome do jogador: ').strip()
nGolsStr = input('Digite o número de gols feitos por ele: ').strip()

if nome == '' and nGolsStr == '':
	ficha()
elif nome == '':
	ficha(nGols = int(nGolsStr))
elif nGolsStr == '':
	ficha(nome=nome)
else:
	ficha(nome, int(nGolsStr))
