# Refazer o 61, para que o usuário possa pedir
# mais X termos depois do final dos 10 termos padrão
# até que o usuário digite 0 para sair .


print('Digite um primeiro termo e uma razão:')
a0 = float(input('>>>\t'))
r  = float(input('>>>\t'))

current = a0

nSteps = 10
totalSteps = 10

while nSteps != 0:

	i = 0
	while i < nSteps:
		print('{} '.format(current))
		current += r
		i += 1

	nSteps = int(input('Imprimir quantos termos? \n>>>\t'))
	totalSteps += nSteps

# print('Um total de {} termos foram mostrados'.format(totalSteps))
print(f'Um total de {totalSteps} termos foram mostrados')
