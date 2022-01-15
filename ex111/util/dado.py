
def leiaDinheiro(prompt):
	aceito = False
	while not aceito:
		try:
			tmp = input(prompt)
			if ',' in tmp:
				tmp = tmp.replace(',','.')
			valor = float(tmp)
			return valor
		except:
			print('ERRO! Digite um valor no formato XXX.XX')
