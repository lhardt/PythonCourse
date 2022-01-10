# Crie um programa para ler uma lista de números.
# Crie 2 listas, a partir dela, para ter os números pares
# e outra para os números ímpares, sem fazer a separação
# logo na leitura.

lista = []
listaPares = []
listaImpares = []

while True:
	try:
		lista.append( int(input('>>> ')) )
	except:
		break

for item in lista:
	if item % 2 == 0:
		listaPares.append(item)
	else:
		listaImpares.append(item)

print(f'Lista:  \t{lista}')
print(f'Pares:  \t{listaPares}')
print(f'Ímpares:\t{listaImpares}')
