# Duas funções:
#  sorteia() -- sorteia 5 números e coloca em uma lista.
#  somaPar() -- soma todos os valores pares em uma lista.
from random import randint

def sorteia():
	lista = []
	for i in range(5):
		lista.append(randint(1,10))
	return lista


def somaPar(lista):
	total = 0
	for it in lista:
		if it % 2 == 0:
			total += it
	return total

lista = sorteia()
print(f'Com a lista sorteada {lista}, teremos um total de {somaPar(lista)} em pares')
