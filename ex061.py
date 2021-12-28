# Refaça o ex 51, da PA, mas usando while.
print('Digite um primeiro termo e uma razão:')
a0 = float(input('>>>\t'))
r  = float(input('>>>\t'))

current = a0
i = 0
while i < 10:
	print('{} '.format(current))
	current += r
	i += 1
