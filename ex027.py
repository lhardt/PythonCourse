# Faça um programa que leia um nome completo
# e mostre, separadamente, o primeiro e o último nome

nomePalavras = input('Digite seu nome:\n>>>\t').split()

if(len(nomePalavras) > 1):
	print('Primeiro nome: \t{}'.format(nomePalavras[0]))
	print('Último nome:   \t{}'.format(nomePalavras[ len(nomePalavras) - 1 ]))
elif(len(nomePalavras) == 1):
	print('Nome único:    \t{}'.format(nomePalavras[0]))
else:
	print('Não há um nome aqui.')
