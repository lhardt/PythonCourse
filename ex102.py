# Uma função chamada fatorial, com um parametro opcional 'show'
# que pode printar a forma de calcular o fatorial.

def fatorial(n, show=False):
	"""
		Calcula o fatorial de um número,
		com a opção de imprimir o cálculo na tela.
		:param int n: o número do qual se quer o fatorial
		:param bool show: Se o cálculo deve ser mostrado na tela
		:return: O fatorial de n
	"""

	result = 1
	if show:
		print('1 ', end='')
	for i in range(2,n+1):
		result *= i

		if show:
			print(f'x {i} ', end='')

	if show:
		print(f'= {result}')

	return result

print(f'O fatorial de 7 é {fatorial(7)}')
print(f'O fatorial de 5 é {fatorial(5,True)}')

help(fatorial)
