# Para importar o reduce, equivalente ao fold funcional.
from functools import reduce

def funcParamCompacto(*compacto):
	print(compacto)

	return (reduce(lambda a,b: a+b, compacto, 0))

def passagemPorRef(num, lista):
	num = num + 7
	lista.append(100)

	return (reduce(lambda a,b: a+b, lista, num))


print('-'*30)

print('Compactação de Parâmetros: ')
somaTotal = funcParamCompacto(5,4,3,2,1)
print(f"A soma total é {somaTotal}")

print('-'*30)


print('Passagem por referência:')
num = 5
lista = [5,4,3]

print(f'Soma result alterado {passagemPorRef(num,lista)}')

print(f'Agora num={num}, lista={lista}')
print(f'número não altera, mas lista sim')
