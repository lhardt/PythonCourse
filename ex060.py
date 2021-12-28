# Mostre o fatorial de um número dado.
def factorial(n):
	total = 1

	if n < 2:
		return total

	# Not using recursion because it's not 'simpler'.
	# Just adds to the stack unnecessarily
	for i in range(1,n+1):
		total *= (i)

	return total


base = int(input('Digite de qual número quer saber o fatorial:\n>>>\t'))
print('O fatorial é {}.'.format(factorial(base)))
