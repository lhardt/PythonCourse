# Crie um programa que lê vários números
# e os coloca em uma lista. Depois disso,
# mostre:
# A) quantos números foram digitados;
# B) a lista de valores ordenada de forma crescente
# C) se o valor 5 foi digitado, e em que posição

lista = []

while True:
	try:
		lista.append(int(input('>>> ')))

	except:
		break

pos5 = -1
if 5 in lista:
	pos5 = lista.index(5)
lista.sort()
print(f'Foram digitados {len(lista)} números')
print(f'A lista de valores é {lista}')
print('O valor 5 foi digitado? {}'.format(f'na {pos5+1}ª posição' if 5 in lista else "não"))
