# Faça um programa que leia algo do teclado,
# e diga todas as informações possíveis sobre
# ela.

valor = input('Digite algo: ')

print('\tO tipo disso é: {}'.format(type(valor)))
print('\tÉ alfabético? {}'.format(valor.isalpha()))
print('\tÉ alfanumérico? {}'.format(valor.isalnum()))
print('\tÉ decimal? {}'.format(valor.isdecimal()))
print('\tÉ numérico? {}'.format(valor.isnumeric()))
print('\tÉ espaço? {}'.format(valor.isspace()))
print('\tÉ maiúsculo? {}'.format(valor.isupper()))
print('\tÉ minúsculo? {}'.format(valor.islower()))
