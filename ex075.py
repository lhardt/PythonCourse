# Leia 4 valores do teclado e inserir
# em uma tupla.
# a) Quantas vezes apareceu o 9
# b) Em que posição apareceu o primeiro 3
# c) Mostrar apenas os pares.
# Crie mensagens de erro apropriadas.
print('Digite 4 números:')


while True:
	try:
		tupla = (
			int(input('>>>\t')),
			int(input('>>>\t')),
			int(input('>>>\t')),
			int(input('>>>\t'))
		)
		break
	except Exception as e:
		print(e)
		print('Tente novamente!')
		continue

print(f'O nove apareceu {tupla.count(9)} vez(es)')

# Ou if 3.in(tupla)
try:
	print(f'O primeiro 3 apareceu em {tupla.find(3)}')
except:
	print('O número 3 não apareceu.')

listaPares = list( filter(lambda x : (x%2 == 0), tupla) )
print(f'Os números pares são { listaPares }')
