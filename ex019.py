# Leia o nome de 4 alunos e sorteie um escolhido
# para apagar o quadro.

from random import randint

nomesAlunos = []

for i in range(4):
    nomesAlunos.append(input('\tNome do aluno {}: '.format(i+1)));

print('Nomes lidos: ')

for i in range(4):
    print('\t' + nomesAlunos[i])

sorteio = randint(0,3)
# também pode ser random.choice(nomesAlunos)
print('O sorteado é ({}) {}'.format(sorteio+1, nomesAlunos[sorteio]))
