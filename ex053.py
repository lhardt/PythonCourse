# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, retirando os
# espaços.
frase = str(input('Digite uma frase: '))

fraseDigest = frase.replace(' ', '').upper()

halfStrSize = len(fraseDigest) // 2

# Eu poderia ter só comparado ela toda com ela toda invertida.
# Não precisava ter recortado.
primeiraParte = fraseDigest[:halfStrSize]
# Lida ao contrário para comparar.
segundaParte = fraseDigest[ :len(fraseDigest) - halfStrSize -1 : -1]

if primeiraParte == segundaParte :
	print('Palíndromo!')
else:
	print('Não é um palíndromo.')
