# Faça um programa que mostre a tabuada
# de cada número que o usuário digitar.
# O programa para quando o usuário digitar
# um valor negativo.

def mostraTabuada(k):
	for i in range(1,11):
		print(f'{k} x {i:2} = {k * i}')

while True:
	try:
		num = int(input('Deseja ver a tabuada de qual número?\n>>>\t').strip())

		if num < 0:
			break

		mostraTabuada(num)
	except:
		break
