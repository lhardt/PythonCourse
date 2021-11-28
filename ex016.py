# Crie um programa que leia um número e
# mostre sua parte inteira.

from math import trunc

val = float(input('Digite um número real: '))

# não precisamos de math.trunc porque o 'from math' tira o namespace.
''' comentário!!! '''
print('O número é {} e parte inteira dele é {}.'.format(val, trunc(val)))
print('O número é {} e parte inteira dele é {}.'.format(val, int(val)))
