# Crie um sistema que guarde uma listagem de pessoas em um arquivo,
# com nome e idade. Ele poderá mostrar a listagem ou guardar uma pessoa
# nova.

import json

def leiaNome(prompt):
	aceito = False
	while not aceito:
		try:
			str = input(prompt).strip()
			if str == '':
				print('ERRO! Valor em branco!')
			else:
				return str
		except KeyboardInterrupt:
			print('O usuário não preencheu o valor')
			return '<desconhecido>'
		except:
			print('ERRO! Digite um valor inteiro')

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


def escreverPessoa():
	pessoa = {}
	pessoa['nome'] = leiaNome('Digite o nome: ')
	pessoa['idade'] = leiaInt('Digite a idade:')
	return pessoa

def salvaLista(lista):
	try:
		out = open('ex114-pessoas.json', 'w')
		out.write(json.dumps(lista))
	except Exception as e:
		print(f'Não foi possível salvar! {e}')


def lerLista():
	try:
		input = open('ex114-pessoas.json', 'r')
		data = json.load(input)
		return data
	except Exception as e:
		print(f'Não foi possível ler! {e}')
		return []


def printLista(lista):
	print('-'*30)
	for p in lista:
		print('{:<25} {:>3}'.format(p['nome'], p['idade']))
	print('-'*30)

lista = lerLista()

while True:
	try:
		opc = int(input('Digite uma opção:\n1- Cadastrar uma pessoa;\n2- Ler lista de pessoas\n>>> '))

		if opc == 1:
			pessoa = escreverPessoa()
			lista.append(pessoa)
			salvaLista(lista)
		elif opc == 2:
			lista = lerLista()
			printLista(lista)
	except KeyboardInterrupt:
		print('\nAté mais!')
		break
	except Exception as e:
		print(f'Erro! {e}')
