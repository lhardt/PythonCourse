
# Tupla / Imutável
print('-' * 20)
print('{:^20}'.format('TUPLAS'))
print('-' * 20)

try:
	# Assim como tudo em Python, não tem restrição de tipo.
	tupla = ('Item', 'Outro', 'Mais um')
	tupla2 = ('a', 'b', 'c', 'd', 5)

	print('Item 1:\t\t{}'.format(tupla[1]))
	print('Item -1:\t{}'.format(tupla[-2]))
	print('Tupla inteira:\t{}'.format(tupla))

	# Para se precisarmos do índice, também dá
	for pos, item in enumerate(tupla):
		print(f'no índice {pos}, temos {item}')

	print(f'Concatenação de duplas: {tupla + tupla2}')

	print('Contar vezes em que aparece: ', tupla.count('Outro'))

	# exception se não achar.
	print('Índice: ', tupla2.index('c'))

	print('Tentando editar: ', end='')


	tupla[2] = 'opa'
except Exception as e:
	print(e)


# Listas
print('-' * 20)
print('{:^20}'.format('TUPLAS'))
print('-' * 20)

try:
	lista = ['Jorge', 'Adão', 'Maria', 'Fabrício']
except Exception as e:
	print(f'Exceção em listas: {e}')
