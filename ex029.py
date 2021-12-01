# Escreva um programa que leia a velocidade de um carro.
# Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa custa R$ 7 para kada km/h acima do limite.

velocidade = int(input('Digite sua velocidade em km/h:\n>>>\t'))

if( velocidade > 80 ):
	print('Multado! o valor da multa é : R$ {}.00'.format(7 * (velocidade - 80)))
else:
	print('Ok...')
