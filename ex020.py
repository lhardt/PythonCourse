# O professor de 4 alunos do ex. passado
# quer sortear a ordem de apresentação dos
# alunos.
# Leia o nome dos 4 alunos e mostre a ordem sorteada.
from random import randint


nomesAlunos = []
ordemApresentacao = []

for i in range(4):
    nome = input('Digite o nome do aluno {}: '.format(1+i))
    nomesAlunos.append(nome)

print('\n')

for i in range(4):
    sorteado = randint(0, 3-i)
    ordemApresentacao.append(nomesAlunos[sorteado])
    nomesAlunos.remove(nomesAlunos[sorteado])

# Era só usar random.shuffle. Eu tinha ficado na curiosidade de mexer com for()
# e listas e acabei nem reparando na 'função pronta'.


for i in range(4):
    print('O {}º aluno a apresentar é {}'.format(i+1, ordemApresentacao[i]))
