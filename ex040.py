# Ex40: MÉDIA
# --------------
# Calcule a média de duas notas.
# Se a média está abaixo de 5, o aluno está 'REPROVADO'
# Abaixo de 7, "EM RECUPERAÇÃO",
# E acima de 7: 'APROVADO'.

print('Digite suas duas notas.')
nota1 = float(input('>>>\t'))
nota2 = float(input('>>>\t'))

notaFinal = (nota1 + nota2) / 2

if notaFinal >= 7:
	print('O aluno está APROVADO.')
elif notaFinal >= 5:
	print('O aluno está EM RECUPERAÇÃO.')
else:
	print('O aluno está REPROVADO.')
