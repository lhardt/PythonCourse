
tupla = ()
lista = []
dicio = {}


dicio['nome'] = 'André'
lista.append(dicio)

print(lista)

print(dicio.keys())
print(dicio.values())
print(dicio.items())

# deep copy
dicio2 = dicio.copy()

for key,val in dicio.items():
	print(f'na posição {key}, temos {val}')
