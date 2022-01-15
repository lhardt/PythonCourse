
def leiaInt(prompt):
	aceito = False
	while not aceito:
		try:
			return int(input(prompt))
		except KeyboardInterrupt:
			print('O usuário não preencheu o número')
			return 0
		except:
			print('ERRO! Digite um valor inteiro')


def leiaFloat(prompt):
	aceito = False
	while not aceito:
		try:
			tmp = input(prompt)
			if ',' in tmp:
				tmp = tmp.replace(',','.')
			valor = float(tmp)
			return valor
		except KeyboardInterrupt:
			print('O usuário não preencheu o número')
			return 0
		except:
			print('ERRO! Digite um valor no formato XXX.XX')


inteiro = leiaInt('Digite um valor inteiro:\n>>>\t')
numreal = leiaFloat('Digite um valor real:\n>>>\t')

print(f'O inteiro foi {inteiro} e o real foi {numreal}')
