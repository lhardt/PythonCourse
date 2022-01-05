# Faça um programa que jogue par ou ímpar;
# O jogo será interrompido quando o
# jogador perder. Mostre o número de
# vitórias consecutivas do jogador.
from random import randint
from time import sleep

# retorna TRUE se quer par.
def getParidadeFromUser():
	inval = ''
	while not inval in ['P', 'I', 'S']:
		inval = input('Você quer par ímpar ou sair? [P/I/S]\n>>>\t').strip().upper()

	if inval == 'S':
		raise Exception('Você desistiu!?')

	return (inval == 'P')

print('Vamos jogar par ou ímpar?')
userGanhou = True
victoryCtr = 0

while userGanhou:
	try:
		paridade = getParidadeFromUser()
		mao = int(input('Digite o valor de sua mão:\n>>>\t'))
		paridadeStr = "par" if paridade else "ímpar"

		# 1..10 tem número igual de pares e ímpares
		maoComputador = randint(1,11)

		# Se pediu par (true) e é divisível (false) ou vice-versa
		userGanhou = ((maoComputador + mao) % 2 == 1) != paridade
		victoryCtr += 1 if userGanhou else 0

		sleep(1)
		print('---------------------')
		sleep(1)
		print(f'Você jogou {mao} e pediu {paridadeStr}. Eu joguei {maoComputador}.')
		sleep(1)
		print('Logo, {}'.format("você ganhou." if userGanhou else "eu ganhei"))

	except Exception as e:
		print(e)
		break

print(f'Foram {victoryCtr} vitórias seguidas.')
print('Até mais!')
