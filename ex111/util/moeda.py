############################
##         EX 107         ##
############################

def aumentar(valor, porc):
	return valor * (1 + porc/100)


def diminuir(valor, porc):
	return valor * (1 - porc/100)


def dobro(valor):
	return 2 * valor


def metade(valor):
	return 0.5*valor

############################
##         EX 108         ##
############################

def moeda(valor):
	return f'R$ {valor:.2f}'


############################
##         EX 109         ##
############################

def aumentar(valor, porc, formatar=False):
	retval = valor * (1 + porc/100)
	return moeda(retval) if formatar else retval


def diminuir(valor, porc, formatar=False):
	retval = valor * (1 - porc/100)
	return moeda(retval) if formatar else retval


def dobro(valor, formatar=False):
	retval = 2 * valor
	return moeda(retval) if formatar else retval


def metade(valor, formatar=False):
	retval = 0.5*valor
	return moeda(retval) if formatar else retval


############################
##         EX 110         ##
############################

def resumo(num, red, aum):
	print('-'*30)
	print('{:^30}'.format('RESUMO DO VALOR'))
	print('-'*30)
	print('{:<21}{}'.format('Preço Analisado:', moeda(num)))
	print('{:<21}{}'.format('Dobro:', dobro(num, True)))
	print('{:<21}{}'.format('Metade:', metade(num, True)))
	print('{:<21}{}'.format(f'Red. de {moeda(red)}:', diminuir(num, red, True)))
	print('{:<21}{}'.format(f'Aum. de {moeda(aum)}:', aumentar(num, aum, True)))

############################

# Aproveitando para testar o pytest também
def test_aumentar():
	assert aumentar(100,50) == 150


# Aproveitando para testar o pytest também
def test_diminuir():
	assert diminuir(100,50) == 50


# Aproveitando para testar o pytest também
def test_dobro():
	assert dobro(100) == 200


# Aproveitando para testar o pytest também
def test_metade():
	assert metade(100) == 50
