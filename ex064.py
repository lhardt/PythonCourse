# Crie um programa que leia vários números inteiros
# até que o usuário digite 999.
# Mostre a soma e a quantidade de números digitados.

totalSum = 0
nTerms = -1
curr = 0
while curr != 999:
	nTerms += 1
	totalSum += curr

	curr = float(input('Digite um número (999 p/ sair):\n>>>\t'))

if nTerms > 0:
	print('A soma é {}, a quantidade é {} e a média é: {}'.format(totalSum, nTerms, totalSum / nTerms))
