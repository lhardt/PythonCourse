# Crie um programa que leia o nome de uma pessoa e mostre:
#	1) O nome com todas as letras maiúsculas,
#   2) O nome com todas as letras minúsculas,
#   3) Quantas letras tem o nome, sem considerar espaços
#   5) Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo:\n>>>\t')).strip()

if(len(nome.replace(' ', '')) > 0):
	print('\tNome maiúsculo:\t{}'.format(nome.upper()))
	print('\tNome minúsculo:\t{}'.format(nome.lower()))
	print('\tQtd Caracteres:\t{}'.format(len(nome)))
	print('\tQuant. Letras: \t{}'.format(len(nome.replace(' ', ''))))
	print('\tQtd. Letras 1º:\t{}'.format(len(nome.split()[0])))
else:
	print("Não há nome!")
