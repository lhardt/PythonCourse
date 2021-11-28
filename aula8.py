# aula sobre imports.
from math import sqrt,ceil,trunc
from random import random
# ou um import normal. 'import math'.


# A aula vai devagar, fui improvisando / vendo na internet
# para dar continuidade
def funcaozinha():
    lido = float(input('Digite um número para ser enraizado: '))

    if (lido > 0):
        print('\tA raiz é : {:.2f}'.format( sqrt(lido) ))
        print('\tE para cima é : {:.2f}'.format( ceil(sqrt(lido)) ))
    else:
        print('Poxa...')


funcaozinha()

def geraParAleatorio(limSup):
    # ou randint(0,limsup)
    return trunc(random() * limSup)  * 2;


print('um número par aleatório é: {}'.format(geraParAleatorio(100)));


# PyPi - Python Package Index.
