# Leia o ano de nascimento de 7 pessoas.
# Diga quantas delas não são maiores e quantas
# já são.
from datetime import datetime

N_TOTAL = 7
IDADE_MAIORIDADE = 18
anoAtual = datetime.now().year

ctrMenores = 0
ctrMaiores = 0

print('Digite 7 anos de nascimento:')

for i in range(N_TOTAL):
	idadeAtual = anoAtual - int(input('{:3}º\t>>>\t'.format(i + 1)))

	if(idadeAtual >= IDADE_MAIORIDADE):
		ctrMaiores += 1
	else:
		ctrMenores += 1

print('Há {} maiores e {} menores de idade aqui.'.format(ctrMaiores,ctrMenores))
