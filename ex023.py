# Faça um programa que leia um número de 0 a 9999 e mostre cada um dos dígitos:
# (milh, cent, dez, uni)

numeroText = input('Digite um número de 0 a 9999\n>>>\t')

if(numeroText.isnumeric()):
	numero = int(numeroText)
	# Poderia usar o strip, converter pra string e str[0], str[1], etc.
	if(numero >= 0 and numero < 10000):
		print(
			"Unidade:\t{:.0f}\nDezena: \t{:.0f}\nCentena:\t{:.0f}\nMilhar: \t{:.0f}".format(
			# Rodaria mais rápido se fizesse o módulo depois, a princípio.
			numero % 10 + 0.0,
			(numero % 100 - numero % 10) / 10,
			(numero % 1000- numero % 100)/100,
			(numero % 10000-numero % 1000)/1000
		))
	else:
		print('Poxa vida...')
else:
	print("POXA!!!!")
