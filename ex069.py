# Leia a idade e sexo de várias pessoas.
# A cada pessoa, pergunte se o usuário quer parar.
# Ao final mostre
# a) Quantos maiores de 18 anos há.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20.
def wantsToLeave():
	result = ''
	while not result in ['S', 'N']:
		result = input('Deseja sair? [S/N]\n>>>\t').strip().upper()

	return result == 'S'

def lerSexo():
	result = ''
	while not result in ['H', 'M']:
		result = input('Sexo [H/M]: ').strip().upper()

	return result


nMenores = 0
nHomens = 0
nJovensMulheres = 0

notExit = True

print('Digite nome e sexo de múltiplas pessoas: ')

while notExit:

	try:
		idade = int(input('Idade:\t').strip())
		sexo = lerSexo()

		nMenores += 1 if (idade < 18) else 0
		nHomens += 1 if (sexo == 'H') else 0
		nJovensMulheres += 1 if (sexo == 'M' and idade < 20) else 0

	except Exception as e:
		print('Erro!')

	notExit = not wantsToLeave()

print(f'O número de menores é {nMenores}')
print(f'O número de homens é {nHomens}')
print(f'O número de mulheres com menos de 20 é {nJovensMulheres}')
