# Crie um programa que leia uma cidade e diga se ela começaom "SANTO"

nome = input('Digite o nome de uma cidade:\n>>>\t')

# Se fosse palavra por palvra, poderia ser .split()[0] == 'santo'
if(nome.strip().upper().find('SANTO') == 0):
	# Ou nome.strip.upper[:5] == 'SANTO'
	print('Começa com Santo!')
else:
	print('Não começa com Santo.')
