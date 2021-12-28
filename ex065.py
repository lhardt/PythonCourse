# Crie um programa que leia vários inteiros.
# Mostre a média, o maior e o menor valores lidos
# O programa pergunta a cada vez se o usuário quer continuar

def wantsToLeave():
	result = ''
	while not result in ['S', 'N']:
		result = input('Deseja sair? [S/N]\n>>>\t').strip().upper()

	return result == 'S'

soma = 0
maior = 0
menor = 0
ctr = 0

continuar = True

while continuar:

	curr = float(input('Digite um número:\n>>>\t'))

	soma += curr

	if ctr == 0:
		maior = curr
		menor = curr
	elif curr > maior:
		maior = curr
	elif curr < menor:
		menor = curr

	ctr += 1

	continuar = not wantsToLeave()

print('----------------')
print('Resultados carregados!')
print('Maior:\t{}'.format(maior))
print('Menor:\t{}'.format(menor))
print('# ins:\t{}'.format(ctr))
print('Soma:\t{}'.format(soma))
print('Média:\t{}'.format(soma / ctr))
