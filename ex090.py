# Faça um programa que leia nome e média de um aluno.
# Guarde também sua situação em um dicionário

aluno = {}

aluno['nome'] = str(input('Nome do Aluno:\t'))
aluno['media'] = float(input(f'Média de {aluno["nome"]}:\t'))
aluno['situacao'] = 'aprovado' if aluno['media'] >= 6 else 'reprovado'

print('Aluno: ')
for k,v in aluno.items():
	print(f'\t{k:12}\t= {v}')
