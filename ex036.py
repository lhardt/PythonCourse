# Ex. 35: EMPRÉSTIMO
# ------------------
# Qual o valor da casa, do salário da pessoa,
# e em quantos anos essa pessoas vai pagar.
#
# Diga se ele pode pagar, considerando que
# ele pode se o valor da parcela for menor
# ou igual a 30% do salário.
valorCasa = float(input('Qual o valor da casa que você deseja?\n>>>\t'))
salario = float(input('Qual é seu salário?\n>>>\t'))
nParc = int(input('Em quantas parcelas deseja pagar?\n>>>\t'))

valorParc = valorCasa / nParc
fracSalario = valorParc / salario

print('Isso significa que você quer pagar em parcelas de ' +
	'R$ {:.2f}, ou seja {:.2f}% do seu salário!'.format(valorParc, fracSalario * 100))

if fracSalario <= 0.3 :
	print('Autorizado! Ele possui renda suficiente')
else:
	print('Empréstimo negado.')

print('------\n')
