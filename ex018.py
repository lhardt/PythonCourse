# Faça um programa que mostre
# o seno, o cosseno e a tangente
# de um número qualquer.

from math import sin,cos,tan

lerqual = (input('Digite r para radianos e g para graus: '))

angulo = 0.0

if(lerqual == "r"):
    angulo = float(input('Digite um valor em radianos: '))
elif(lerqual == "g"):
    angulo =  ( 3.141598 / 180 ) * float(input('Digite um valor em graus: '))



print('\tO SEN do ângulo é : {:.3f}'.format( sin(angulo) ))
print('\tO COS do ângulo é : {:.3f}'.format( cos(angulo) ))
print('\tA TAN do ângulo é : {:.3f}'.format( tan(angulo) ))
