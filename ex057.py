# Faça um programa que leia o sexo de uma pessoa
# Só aceite M ou F. Se for errado, tente novamente
# até dar certo.

sexo = '0'

while sexo != 'M' and sexo != 'F':
	sexo = str(input('Digite o sexo (\'M\' ou \'F\'):\n>>>\t')).upper()

print('O sexo final é <{}>\n'.format(sexo));
