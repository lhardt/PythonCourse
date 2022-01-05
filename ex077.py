# Crie um programa que tenha uma tupla com várias
# palavras, sem acento. Mostre, para cada palavra
# quais são suas vogais.

def isVogal(letra):
	try:
		index = ['a','e','i','o','u'].index(letra.lower())
		return True
	except:
		return False

def getVogais(palavra):
	return list(filter(isVogal, palavra))

palavras = (
	'atomo', 'abacaxi', 'filosofia', 'estudo', 'faca',
	'garfo', 'historia', 'literatura', 'organismo', 'portugal'
)

for i, vogais in enumerate(map(getVogais, palavras)):
	print(f'Em {palavras[i]:15}{vogais}')

print('\n	')

# Ou
for palavra in palavras:
	print(f'\nEm {palavra:15}, ', end='')

	for letra in palavra:
		if letra.lower() in 'aeiou':
			print(letra, end=' ')
