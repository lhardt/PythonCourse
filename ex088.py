# Faça um programa criador de
# palpites da mega sena (de 1 a 60).
# Sorteie números de 1 a 60 para fazer
# um palpite (6 números). Coloque quantos
# palpites o usuário quiser dentro de uma lista
# e a imprima.

from random import randint


def criaPalpite():
	palpite = []

	for i in range(6):
		num = randint(1,61)
		while num in palpite:
			num = randint(1,61)

		palpite.append(num)

	return palpite

while True:
	try:
		print('Quantos palpites vc quer? Digite 0 para sair')
		nPalpites = int(input('>>> '))

		if nPalpites <= 0:
			break

		palpites = []

		print('Seus palpites são: ')

		for i in range(nPalpites):
			palpite = criaPalpite()
			while palpite in palpites:
				palpite = criaPalpite()

			palpites.append(palpite)

			print(f'\t{palpite}')


	except Exception as e:
		print(f'Erro! {e}')
