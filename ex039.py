# Ex39: ALISTAMENTO
# -----------------------
# Faça um programa que leia o ano de nascimento de um jovem e diga:
# - Se ele ainda vai se alistar no Exército
# - Se já é hora de se alistar
# - Se já passou do tempo de alistamento.

from datetime import datetime

ANO_ATUAL = datetime.now().year

nascAlist = ANO_ATUAL - 18
nascUser = int(input('Digite seu ano de nascimento:\n>>>\t'))

print('O ano atual é {}'.format(ANO_ATUAL))

if nascUser == nascAlist:
	print('SE ALISTE! PATRIA AMADA! ')
elif nascUser < nascAlist:
	print('Se você não se alistou, regularize sua situação com as forças armadas.')
else:
	print('O pior ainda está por vir...')
