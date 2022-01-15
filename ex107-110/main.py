import moeda

valor = float(input('Digite um preço:\n>>>\t'))

print('-'*30)

############################
##         EX 107         ##
############################

print(f'O valor originalmente é R$ {valor:.2f}')
print(f'Aumentando em 30% temos R$ {moeda.aumentar(valor,30):.2f}')
print(f'Descontando 15% teremos R$ {moeda.diminuir(valor,15):.2f}')
print(f'A metade é: R$ {moeda.metade(valor):.2f}')
print(f'O dobro  é: R$ {moeda.dobro(valor):.2f}')

############################
##         EX 108         ##
############################

print('-'*30)

print(f'Aumentando em 30% temos {moeda.moeda(moeda.aumentar(valor,30))}')
print(f'Descontando 15% teremos {moeda.moeda(moeda.diminuir(valor,15))}')
print(f'A metade é: {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro  é: {moeda.moeda(moeda.dobro(valor))}')

############################
##         EX 109         ##
############################

print('-'*30)

print(f'Aumentando em 30% temos {moeda.aumentar(valor,30, True)}')
print(f'Descontando 15% teremos {moeda.diminuir(valor,15, True)}')
print(f'A metade é: {moeda.metade(valor, True)}')
print(f'O dobro  é: {moeda.dobro(valor, True)}')

############################
##         EX 110         ##
############################

moeda.resumo(valor,50,20)
