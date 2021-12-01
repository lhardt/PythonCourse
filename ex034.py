# Escreva um programa que pergunte
# o salário de um funcionário e calcule seu aumento.
#
# Para salários maiores que 1250, calcule um aumento de 10%
# Para os inferioes ou iguais, o aumento é de 15%.

salarioOriginalStr = str(input('Digite seu salário original: \n>>>\tR$ '))

try:
	salarioOriginal = float(salarioOriginalStr)
	multiplicador = 1.10 if (salarioOriginal > 1250) else 1.15
	salarioFinal = salarioOriginal*multiplicador
	print('Seu aumento é de {:.2f}% e seu salário final é de R$ {:.2f}.\n'.format(100*(multiplicador - 1), salarioFinal))
except ValueError:
	print('Insira como R$ XXXX.XX')
