# Faça e chame uma função area, que receba as dimensões de um terreno retangular
# e mostre sua área.

def area(x,y):
	return x*y

print('Digite a largura e o comprimento do terreno.')
x = float(input('>>> '))
y = float(input('>>> '))

print(f'A área total é de {x}m x {y}m = {area(x,y)}m')
