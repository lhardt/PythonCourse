# Crie uma função chamada contagem, com parâmetros início fim e passo.
# Ela deve contar do início até o fim, de passo em passo (ué)
# Faça 3 contagens
# a) 1 a 10, de 1 em 1
# b) 10 a 0, de 2 em 2

def contagem(start,step,end):
	i = start
	print(i, end=' ')
	while abs(end-i) > abs(end-i-step):
		i += step
		print(i, end=' ')
	print()


contagem(0,1,10)
contagem(10,-1,0)

print('Digite, nesta ordem, início, passo e fim')
start = int(input('>>>\t'))
step = int(input('>>>\t'))
end = int(input('>>>\t'))

contagem(start,step,end)
