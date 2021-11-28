# Crie um programa que, a partir do tamanho
# dos dois catetos de um triângulo retângulo,
# dê o tamanho da hipotenusa.

# Poderia ser (x ** (1/2)) também, mas é menos legível
from math import sqrt

cat1 = float(input('Digite o comprimento do 1º cateto (cm): '))
cat2 = float(input('Digite o comprimento do 2º cateto (cm): '))

if(cat1 > 0 and cat2 > 0):
    hip = sqrt(cat1 ** 2 + cat2 ** 2)

    print('O tamanho da hipotenusa é {:.2f}.'.format(hip))
else:
    print('Valores inválidos!')
