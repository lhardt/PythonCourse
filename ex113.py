# Teste e diga se o site do Pudim está acessível.
from urllib import request


print('O site do Pudim está acessível?', flush=True)

try:
	response = request.urlopen(request.Request('http://pudim.com.br'))
	print(f'Sim! {response}')
except Exception as ex:
	print('Não!')
	print(f'Erro! {ex}')
