# Faça um programa que leia um ano qualquer e mostre
# se ele é bissexto.

anostr = str(input('Digite um ano:\n>>>\t'))

if anostr.isnumeric():
	ano = int(anostr)
	# Múltiplos de 4, mas não de 100, ou também de 400.
	bissexto = (ano % 4 == 0) and (ano % 400 == 0  or (not ano % 100 == 0))
	print('O ano é bissexto? {};\n'.format("sim" if bissexto else "não"))
