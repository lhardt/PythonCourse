# Um manual interativo, em que o usuário dá o nome de um comando
# e o programa mostra o manual dele.

while True:
	inval = input('Digite um comando ou em branco para sair.\n>>>\t').strip()

	if inval == '':
		break

	help(inval)
