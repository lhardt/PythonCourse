# Refazer o desafio 28, (agora números de 0 a 10)
# para que o usuário fique tentando até acertar e,
# ao final, mostrar o número de palpites necessários
from random import randint

shouldContinue = True

print('Digite -1 para parar.')

while shouldContinue:
	numero = randint(0,11)
	print('Pensei em um novo número de 0 a 10. Tente acertá-lo!')

	nTentativas = 1
	digitado = input('>>>\t').strip()
	# De forma que digitar uma string não crasha na conversão.
	while str(numero) != digitado and digitado != '-1':
		digitado = input('>>>\t').strip()
		nTentativas += 1

	if digitado == '-1':
		break

	print('Você acertou em {} tentativas!'.format(nTentativas))

	if nTentativas < 4:
		print('Essa foi boa!')
	elif nTentativas > 8:
		print('Pouca sorte!')
