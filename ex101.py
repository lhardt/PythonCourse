# Função voto que, a partir de um ano de nascimento, retorna
# um literal entre NEGADO, OBRIGATÓRIO e OPCIONAL nas eleições.
from datetime import datetime

anoCorrente = datetime.now().year

def voto(ano):
	idade = anoCorrente - ano
	if idade >= 60:
		return 'OPCIONAL'
	if idade >= 18:
		return 'OBRIGATÓRIO'
	if idade >= 16:
		return 'OPCIONAL'
	return 'NEGADO'

nasc = int(input('Digite seu ano de nascimento:\n>>>\t'))

print(f'Seu voto é {voto(nasc)}')
