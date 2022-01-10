# Crie um programa em que o usuário possa
# digitar vários números e os cadastre em
# uma lista. Caso o número já exista, não
# o adicione. Ao final,  mostrar todos os
# valores únicos digitados de forma cres-
# cente.

print('Digite quantos números quiser.')
print('Caso queira sair, só deixe em branco e aperte <ENTER>')

lista = []

while True:
	try:
		valor = (int(input('>>> ')))

		if not valor in lista:
			lista.append(valor)

	except Exception as e:
		break

lista.sort()
print(f'Os valores digitados são {lista}!')
