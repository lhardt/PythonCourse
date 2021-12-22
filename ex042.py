# Ex42: TRIANGULOS
# ------------------
# Diga o tipo de um triângulo, a partir de 3 comprimentos:
# Equilátero, Isósceles, Escaleno ou Impossível.
# Vide exercício 35.

print('Digite 3 números, lados de um triângulo.')

lados = []

for i in range(3):
	lados.append(float(input('>>>\t')))

isTriangle = (lados[0] < lados[1] + lados[2]
		  and lados[1] < lados[2] + lados[0]
  		  and lados[2] < lados[0] + lados[1])

tipoTriangulo = 'impossivel'

if isTriangle:
	nIgualdades = 0

	for i in range(3):
		for j in range(i+1, 3):
			if lados[i] == lados[j]:
				nIgualdades += 1

	switcher = {
		0: 'Escaleno',
		1: 'Isósceles',
		# Impossível duas igualdades sem haver uma terceira.
		3: 'Equilátero'
	}

	tipoTriangulo = switcher.get(nIgualdades)


print('O triangulo é: {}'.format(tipoTriangulo))
