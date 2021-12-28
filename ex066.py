# Crie um programa que leia vários números
# inteiros e só pare na digitação do 999.
# Mostre o # de números e a soma deles,
# sem contar o 999

soma = 0
ctr = -1
read = 0

print('Digite quantos números quiser [999 para parar]')

while read != 999:
	try:
		ctr += 1
		soma += read

		read = int(input('>>>\t'))
	except:
		break

print(f'Foram digitados {ctr} números e a soma é {soma}.')
