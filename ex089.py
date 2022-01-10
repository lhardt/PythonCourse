# Crie um programa que leia nome e 2 notas (e guarde também a média)
# de vários alunos (lista-de-listas-de-listas)
# Mostre um boletim com a média de cada aluno
# e dê a opção para ver todas as notas de um
# aluno.

def lerAluno():
	aluno = []

	nome = input('Digite o nome do aluno:\n>>> ')
	if nome == '':
		raise Exception('Erro de inserção.')

	nota1 = float(input('Digite as duas notas\n>>> '))
	nota2 = float(input('>>> '))
	media = (nota1 + nota2)/2

	aluno.append(nome)
	aluno.append([nota1,nota2])
	aluno.append(media)

	return aluno

def alunoString(aluno):
	return (f'{aluno[0]}\t[Média: {aluno[2]}, Notas: {aluno[1]}]')

alunos = []
while True:
	try:
		alunos.append( lerAluno() )
	except Exception as e:
		print('Erro! Deixando de cadastrar alunos...')
		break


print(f'Foram inseridos {len(alunos)} alunos!')
print('Os alunos lidos foram: ')
for aluno in alunos:
	print(f'\t{alunoString(aluno)}')
