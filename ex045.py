# Crie um jogo de Jokenpô.
from random import randint

jogar = True;

def getEscolhaJogador():
	while True:
		try:
			print('Escolha sua mão')
			print('1. Pedra')
			print('2. Papel')
			print('3. Tesoura')
			print('4. Sair')
			escolha = int(input('>>>\t'))

			return escolha
		except IOException:
			print('Opção Inválida!')

def formatEscolha(escolha):
	switcher = {
		1: 'Pedra',
		2: 'Papel',
		3: 'Tesoura'
	}

	return switcher.get(escolha)

GANHADOR_EMP = 0
GANHADOR_MAQ = 1
GANHADOR_JOG = 2

GANHADOR_SWITCHER = {
	0: "Empate",
	1: "Máquina",
	2: "Jogador"
}

# A máquina tem o primeiro score, o player tem o segundo
PLAYER_SCORE_SWITCHER = {
	1: 1,
	2: 0
}

def quemGanhaCod(escolhaJogador, escolhaMaquina):
	if escolhaJogador == escolhaMaquina:
		return GANHADOR_EMP
	if escolhaJogador == 1:
		return GANHADOR_MAQ if escolhaMaquina == 2 else GANHADOR_JOG
	if escolhaJogador == 2:
		return GANHADOR_MAQ if escolhaMaquina == 3 else GANHADOR_JOG
	if escolhaJogador == 3:
		return GANHADOR_MAQ if escolhaMaquina == 1 else GANHADOR_JOG

placar = [0,0]

while jogar:
	escolhaJogador = getEscolhaJogador()
	escolhaMaquina = randint(1,3)


	if escolhaJogador == 4:
		jogar = False
	else:
		print('Você escolheu {} e eu escolhi {}'.format(
			formatEscolha(escolhaJogador),
			formatEscolha(escolhaMaquina)))

		ganhadorCod = quemGanhaCod(escolhaJogador, escolhaMaquina)

		print('Quem ganhou foi: {}'.format(GANHADOR_SWITCHER.get(ganhadorCod)))

		if ganhadorCod != GANHADOR_EMP:
			placar[ PLAYER_SCORE_SWITCHER.get(ganhadorCod) ] += 1

		print('Score atual: Máquina {} vs Jogador {}'.format(placar[1], placar[0]))
