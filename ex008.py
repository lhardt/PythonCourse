# Escreva um programa que leia um valor
# em metros, e mostre ele em centímetros
# e milímetros.
n1 = float(input('Valor em metros: '))

print('\tValor em kilômetros: {}'.format(n1 / 1000))
print('\tValor em hectômetros: {}'.format(n1 / 100))

print('\tValor em centímetros: {}'.format(n1 * 100))
print('\tValor em milimetros: {}'.format(n1 * 1000))
