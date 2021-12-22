# Ex043: Leia o peso e a altura de uma pessoa.
# Se o IMC for menor que 18.5, 'Abaixo do Peso'
# Se o IMC for menor que 25, 'Peso Ideal'
# Se o IMC for até 30, 'Sobrepeso'
# Se o IMC for até 40, 'Obesidade'
# Se o IMC for maior, 'Obesidade Morbida'

print('Digite sua altura (m) e depois seu peso (kg)')

altura = float(input('>>>\t'))
peso = float(input('>>>\t'))

imc = peso / (altura ** 2)

print('Seu IMC é : {:.1f}'.format(imc))

categoria = 'Obesidade Morbida'

if imc < 18.5:
	categoria = 'Abaixo do Peso'
elif imc < 25:
	categoria = 'Peso Ideal'
elif imc < 30:
	categoria = 'Sobrepeso'
elif imc < 40:
	categoria = 'Obesidade'

print('Ou seja, você está na categoria \"{}\"'.format(categoria))
