# Fala um programa que leia a largura e altura
# de uma parede, em metros, e calcule a sua área,
# bem como a quantidade de tinta necessária para
# pintar, supondo que 1L rende 2m^2 de parede.

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

area = altura * largura
tinta = area / 2

print('A parede tem {} m^2, e usaria {} L de tinta'.format(
    area, tinta
))
