# Crie um programa em que o usuário digite
# uma expressão numérica qualquer.
# Diga se a ordem dos parênteses está correta,
# e se todo aberto está fechado.

str = input('Digite uma expressão matemática\n>>>\t')

nAbertos = 0
valido = True
for ch in str:
	if ch == '(':
		nAbertos += 1
	elif ch == ')':
		nAbertos -= 1

		if nAbertos < 0:
			valido = False

# Ao final, todos abertos devem ter sido fechados.
valido = valido and nAbertos == 0


print('A expressão é válida?', 'sim' if valido else 'não')
