# Crie um programa que leia 2 valores e mostre
# um menu: somar, multiplicar, maior, digitar
# novos números e sair.

OPT_SUM = 1
OPT_MULT = 2
OPT_NEWNUMBERS = 3
OPT_LEAVE = 4

def mostrarMenu():
	print('Selecione uma opção: ')
	print('[ 1 ] Somar números carregados')
	print('[ 2 ] Multiplicar números carregados')
	print('[ 3 ] Carregar novos números')
	print('[ 4 ] Sair')

	read = ''
	while not read in ['1','2','3','4'] :
		read = input('>>>\t').strip()

	return int(read)

def getNewNumbers():
	tryAgain = True
	n1 = 0
	n2 = 0
	while tryAgain:
		try:
			print('Digite dois números: ')
			n1 = float(input('>>>\t'))
			n2 = float(input('>>>\t'))
			tryAgain = False
		except:
			print('Digite NÚMEROS0! Um de cada vez')
	return [n1,n2]


a = 0
b = 0
option = 3
while option != OPT_LEAVE:
	if option == OPT_NEWNUMBERS:
		[a,b] = getNewNumbers()
	elif option == OPT_SUM:
		print('A soma de {} e {} é {}'.format(a,b,a+b))
	elif option == OPT_MULT:
		print('A multiplicação de {} e {} é {}'.format(a,b,a*b))
	elif option == OPT_LEAVE:
		print('Até mais!')
		break

	option = mostrarMenu()
