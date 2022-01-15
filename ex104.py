# Crie a função leiaint(), que faça a validação para só aceitar valor numérico

def leiaint(prompt):
	aceito = False
	while not aceito:
		try:
			num = int(input(prompt))
			return num
		except:
			print('ERRO! Digite um número inteiro.')


numero = leiaint('Oi. Digita aí um numero\n>>>\t')
print(f'Você digitou {numero}')
