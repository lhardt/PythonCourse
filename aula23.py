

try:
	a = int(input('Digite um número\n>>>\t'))

except Exception as e:
	print(f'Opa. {e.__class__}')
# Outros Excepts.
else:
	print(f'a = {a}')
finally:
	print('Deseja continuar?')
