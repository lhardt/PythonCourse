# Crie  um  programa que tenha uma tupla
# totalmente preenchida com uma contagem
# de 0 a 20 por extenso.  Leia um número
# pelo teclado, e mostre esse número por
# extenso.   'Tente novamente'   até   o
# usuário digitar um número corretamente.

stringifiedNumbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
	'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
	'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

error = True
while error:
	try:
		number = int(input('Digite um número de 0 a 20: '))

		if number >= 0 and number <= 20:
			print(f'O número por extenso é {stringifiedNumbers[number]}')
			error = False
		else:
			print('Tamanho errado! ', end='')

	except Exception:
		print('um NÚMERO inteiro! ', end='')
		continue
