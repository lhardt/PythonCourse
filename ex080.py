# Crie um programa em que o usuário digite 5 valores.
# Coloque-os na posição correta sem usar o sort.

lista = []

for iValor in range(5):
	valor = int(input('Digite um valor: '))

	inseriu = False

	for iLista in range( len(lista) ):
		if valor < lista[iLista]:
			lista.insert(iLista, valor)
			inseriu = True
			break

	if not inseriu:
		lista.append(valor)

print(f'A lista em ordem é {lista}.')
