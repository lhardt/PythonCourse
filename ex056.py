# Leia nome, idade e sexo de 4 pessoas.
# No final o programa mostra:
# - A média de idade,
# - O nome do HOMEM mais velho,
# - Quantas mulheres tem menos de 20 anos.

print('Digite NOME, IDADE, e SEXO de 4 pessoas:')

somaIdade = 0
idadeVelho = 0
nomeVelho = ''
nMulheresNovas = 0

for i in range(4):
	nome  = str(input('Nome:\t\t>>>\t'))
	idade = int(input('Idade:\t\t>>>\t'))
	sexo =  str(input('Sexo:[F/M]\t>>>\t')).lower()

	print('-------------')

	somaIdade += idade

	if idade < 20 and sexo == 'f':
		nMulheresNovas += 1
	elif sexo == 'm' and idadeVelho < idade:
		nomeVelho = nome
		idadeVelho = idade

mediaIdade = somaIdade / 4

print('Média de idade inserida: {}'.format(mediaIdade))
print('Nº de mulheres com menos de 20: {}'.format(nMulheresNovas))

if idadeVelho != 0:
	print('Nome do homem mais velho: {}({})'.format(nomeVelho,idadeVelho))
