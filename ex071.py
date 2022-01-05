# Crie um programa que simule o funcionamento
# de um caixa eletrônico. Pergunte qual é o
# valor a ser sacado e diga qual a quantidade
# de cada cédula deverá ser entregue.
# Cédulas disponíveis: 50, 20, 10, 1.

try:
	valorARetirar = int(input('Digite um valor inteiro a ser sacado:'))

	valorCedulas = [50, 20, 10, 1]
	qtdCedulas = [0,0,0,0]

	for i in range(len(valorCedulas)):
		qtdCedulas[i] = valorARetirar // valorCedulas[i]
		valorARetirar -= qtdCedulas[i] * valorCedulas[i]

	# Imprimir - poderia ser o mesmo for() sem uma lista, mas
	# assim parece mais aplicável.

	for i in range(len(valorCedulas)):
		print(f'{qtdCedulas[i]:2} cédulas de {valorCedulas[i]} ')

except Exception as e:
	print(f'Opa! {e}')
