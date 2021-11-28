# ----------------------
# Operadores
# ----------------------
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Adição e Subtração
print('\t{} +  {} == {}'.format(n1,n2, n1+n2))
print('\t{} -  {} == {}'.format(n1,n2, n1-n2))

# Multiplicação e Potência
print('\t{} *  {} == {}'.format(n1,n2, n1*n2 ))
print('\t{} ** {} == {}'.format(n1,n2, n1**n2 ))
print('\t{} ** {} == {:.3f}'.format(n1,0.5, n1**0.5 ))

# Divisão
print('\t{} /  {} == {:.3f}'.format(n1,n2, n1 / n2 ))

# Divisão Inteira
print('\t{} // {} == {}'.format(n1,n2, n1 // n2 ))

# Resto
print('\t{} %  {} == {}'.format(n1,n2, n1 % n2 ))

# Repetição de strings:
print( '=' * 20)

# ----------------------
# Ordem de Precedência
# ----------------------
# 1º.  (   )
# 2º.  **
# 3º.  *  /  //  %
# 4º. +  -

# ----------------------
# Macetes do print:
# ----------------------

# Alinhamento

print('<{:^10}>, <{:<10}>, <{:>10}>'.format('Léo', 'Léo', 'Léo'))
print('<{:=^10}>, <{:_<10}>, <{:X>10}>'.format('Léo', 'Léo', 'Léo'))
print('Oi ', end='')
print('Leo')
