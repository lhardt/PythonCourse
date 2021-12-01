# Faça um programa que leia uma frase do telcado e mostre:
#  i) quantas vezes aparece a letra A,
# ii) Em que posição ela aparece pela primeira vez.
#iii) Em que posição ela aparece pela última vez

texto =input('Digite uma frase qualquer.\n>>>\t').lower()
numa = texto.count('a')

if( numa > 0 ):
	print('A letra \'A\' aparece {} vezes!'.format( texto.count('a') ))
	print('A letra \'A\' aparece pela primeira vez em {}!'.format( texto.find('a')))
	print('A letra \'A\' aparece pela última vez em {}!'.format( texto.rfind('a')))
else:
	print('A letra \'A\' não aparece ... ')
