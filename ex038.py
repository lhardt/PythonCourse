# Ex38: MAIOR E MENOR
# ------------------------------
# Escreva um prog que leia dois números inteiros.
# Diga "O 1º número é maior", "O 2º n. é maior" ou "Os números são iguais."
print("Digite dois números: ")

num1 = float(input('>>>\t'))
num2 = float(input('>>>\t'))

if num1 == num2:
	print('Os números são iguais.')
elif num1 > num2:
	print('O primeiro número é maior.')
else:
	print('O segundo número é maior.')
