# Leia o 1º termo e a razão de uma P.A.
# Mostre os 10 primeiros termos.
print('CALCULADORA DE PROGRESSÃO ARITMETICA')
print('------------------------------------')

a0 = float(input('Digite o termo inicial:\n>>>\t'))
r  = float(input('Digite a razão:\n>>>\t'))

print('------------------------------------')
print('Os 10 primeiros termos são: ')

termo = a0

for i in range(10):
	print('{:3}º termo é {:4}'.format(i+1, termo))
	termo += a0
