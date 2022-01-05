# Crie um programa que crie 5 números aleatórios
# e guarde em uma tupla. Depois, mostre a
# listagem deles, o maior e o menor.
from random import randint

LIM = 30

print(f'Gerando 4 números aleatórios com limite {LIM}: ')

tupla = (randint(0,LIM),randint(0,LIM),randint(0,LIM),randint(0,LIM))

print(f'Os números gerados são: {tupla}')

max = tupla[0]
min = tupla[0]

for i in range(1, 4):
	if max < tupla[i]:
		max = tupla[i]
	if min > tupla[i]:
		min = tupla[i]

# Ou max = max(tupla)
# Ou min = min(tupla)

print(f'O máximo é {max} e o mínimo é {min}')
