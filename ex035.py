# Desenvolva um programa que leia o comprimento de 3 retas e diga
# se elas podem formar um triângulo.
# Cond:

a = float(input('Digite o tamanho do lado 1: '))
b = float(input('Digite o tamanho do lado 2: '))
c = float(input('Digite o tamanho do lado 3: '))

if ((a < b+c) and (b < a+c) and (c < a+b)):
	print('Pode formar um triângulo!')
else:
	print('Não pode formar um triângulo.')
