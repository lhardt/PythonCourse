# ----------------------
# Tipos Primitivos
# ----------------------
# int, float, bool e str.

strn1 = input('Primeiro num: ')
strn2 = input('Segundo num: ')

# Dá a concatenação desses dois números.
print('\tA concatenação é ', strn1 + strn2)

if( strn1.isnumeric() and strn2.isnumeric() )
    n1 = int(strn1)
    n2 = int(strn2)

    print('\tA soma é', int(strn1) + int(strn2))
    print('\tA soma entre {} e {} vale {}: '.format(n1, n2, n1+n2))

booleano = (5 == 8)
print('\tSe eu tiver um booleano : ', str(booleano))
print('\tOs valores booleanos são : ', True, 'e', False)

flutuante = 3.005
flutstring = '7.05'
print('\tSoma de floats: {}'.format(flutuante + float(flutstring)))

print('Tipos: ', type(booleano), type(strn1), type(n2), type(flutuante))
