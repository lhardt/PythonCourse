# Refaça o exercício (9).
base = int(input('Digite um número para conhecer sua tabuada: \n>>>\t'))

for i in range(1,11):
	print('{} x {:2} = {}'.format(base,i, base*i))
