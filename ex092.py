# Crie um programa que leia nome, ano de nasc.
# e CTPS de um usuário, e os cadastre (com idade)
# Se a ctps não for 0, informar também o ano de
# contratação e salário. Calcule e acrescente,
# daqui quanto tempo a pessoa vai se aposentar
# (35 anos de trabalho)
from datetime import datetime

anoAtual = datetime.now().year

pessoa = {}
pessoa['nome'] = str(input("Nome: "))
pessoa['anoNasc'] = int(input("Ano de Nascimento: "))
pessoa['ctps'] = input("CTPS (em branco se não houver): ")

if pessoa['ctps'].strip() != '':
	pessoa['anoContrato'] = int(input('Ano de contratação: '))
	pessoa['salario'] = float(input('Salário: '))

	pessoa['tempoAposentar'] = 35 - (anoAtual - pessoa['anoContrato'])


print(pessoa)
