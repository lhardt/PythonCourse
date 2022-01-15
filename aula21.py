


def funcaoDocumentada(a,b):
	"""
	Dá a soma de dois números.
	:param int a: Um valor numérico
	:param int b: Um valor numérico
	:return: A soma de a e b
	"""
	return a+b

def paramOpcional(a=0,b=0,c=0):
	return a+b+c

def paramSilencioso():
	# valorNoEscopo é global.
	print(f'Fora do escopo, {valorNoEscopo}')
	# Mas se eu desse valorNoEscopo = 5,
	# aí haveria uma variavel local com esse mesmo nome por aqui,
	# porque conta como uma nova definição. A não ser que eu faça isso:
	global valorNoEscopo
	valorNoEscopo = 8


# help(print)
print(print.__doc__)


# help(funcaoDocumentada)
print(funcaoDocumentada.__doc__)

print(f'Soma: {paramOpcional(c=1,a=2)}')


valorNoEscopo = 6
print(f'No escopo, {valorNoEscopo}')
paramSilencioso()
