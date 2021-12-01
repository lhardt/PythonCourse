# Crie um programa para dizer se há 'silva' no nome de alguém

nome = input('Digite seu nome:\n>>>\t')

if('SILVA' in nome.upper().split()):
	print('é silva!!!')
else:
	print('Não é silva...')
