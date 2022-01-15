# Faça uma função 'notas', que receba um varargs de notas,
# e que retorna um dicionário com as seguintes informações:
# a) maior nota;
# b) menor nota;
# c) a média da turma;
# d) a situação, opcionalmente.

# Para importar o reduce, equivalente ao fold funcional.
from functools import reduce

def notas(*notas, sit=False):
	relatorio = {}
	relatorio['total'] = len(notas)
	relatorio['max'] = max(notas)
	relatorio['min'] = min(notas)
	relatorio['media'] = reduce(lambda a,b: a+b, notas, 0)/len(notas)

	if sit:
		relatorio['situacao'] = "BOA" if relatorio['media'] > 6 else "RUIM"
	return relatorio


print(notas(5,3,1,2, sit=True))
