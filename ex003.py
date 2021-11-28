# Dar a soma de dois números

strn1 = input('Primeiro num: ')
strn2 = input('Segundo num: ')
n1 = int(strn1)
n2 = int(strn2)
# Dá a concatenação desses dois números.
print('A concatenação vale: ', strn1 + strn2)
print('A soma vale: ', int(strn1) + int(strn2))
print('A soma entre ', strn1, 'e', strn2, ' vale: ', int(strn1) + int(strn2))
print('A soma entre {} e {} vale {}: '.format(n1, n2, n1+n2))
