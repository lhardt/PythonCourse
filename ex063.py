# Leia N e mostre os primeiros N números de fibonacci
def fibonacci(n):
	# Two terms behind
	aux = 0
	# One term behind
	prev = 0
	# Current Term
	curr = 1
	# Counter
	i = 0

	while i < n:
		aux = prev
		prev = curr
		curr = aux + prev
		i += 1
		print('{}º:\t{}'.format(i, curr))

	return curr


n = int(input('Qual é o termo de fibonacci?\n>>>\t'))

print(' ') # One line for visualization
fibonacci(n)
