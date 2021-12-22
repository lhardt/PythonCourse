# Ex037: CONVERSÃO
# ------------------
# Leia um número inteiro e peça para o usuário
# escolher uma base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal.

numero = int(input('Digite um numero:\n>>>\t'))

print('Escolha uma base de conversão:')
print('1- Binário')
print('2- Octal')
print('3- Hexadecimal')

base = int(input('>>>\t'))

if base == 1:
	print('Convertendo...  {:b} na base binária.'.format(numero))
elif base == 2:
	print('Convertendo... {:o} na base octal.'.format(numero))
elif base == 3:
	print('Convertendo... {:x} na base hexadecimal.'.format(numero))

print('Fim.\n')
