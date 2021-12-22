# Diga, a partir do ano de nascimento de um atleta,
# a categoria dele:
# até 9 anos: 'MIRIM'
# até 14 anos: 'INFANTIL'
# até 19 anos: 'JUNIOR'
# até 40 anos: 'SENIOR'
# senão: 'MASTER'

from datetime import datetime

anoNasc = int(input('Digite seu ano de nascimento\n>>>\t'))

idade = datetime.now().year - anoNasc

categoria = 'MASTER'

if idade <= 9:
	categoria = 'MIRIM'
elif idade <= 14:
	categoria = 'INFANTIL'
elif idade <= 19:
	categoria = 'JUNIOR'
elif idade <= 40:
	categoria = 'SENIOR'

print('Sua categoria é {}.'.format(categoria))
