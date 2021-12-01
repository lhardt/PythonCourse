# Manipulação de texto.
texto = "Lorem ipsum dolor sit amet."


# Acesso
print( 'Primeiro Caracter:\t',  texto[0] )

# Repara que texto[11] não entra
print( 'Segunda Palavra: \t',  texto[6:11] )

# Ignora depois de terminar. Não há 40 caracteres.
print( 'Estouro Limite: \t',  texto[12:40] )

# Saltando de 2 em 2.
print( 'Segunda Palavra: \t',  texto[4:10] )
print( 'De 2 em 2 carct: \t',  texto[4:10:2] )

# fatiar com parametros implicitos
print('Fatiando s/ Inic: \t', texto[:5])
print('Fatiando s/ fim:  \t', texto[10:])
print('Fatiando pulando:  \t', texto[:10:2])

# Funçõeszinhas
print('Tamanho: \t\t', len(texto) )
# print('Tamanho: \t\t', texto.len() ) Não funciona
print('Cont.  de \'i\':\t\t', texto.count('i'))
print('Cont.  de \'i\':\t\t', texto.count('i',0,10)) # Posição 10 não inclui
print('Onde é \'lor\':\t\t', texto.find('lor'))
print('Onde é \'XYZ\':\t\t', texto.find('XYZ'))

print('Existe \'ipsum\'?\t\t', 'ipsum' in texto )


# mesma coisa com .upper e .lower
texto2 = texto.replace('amet', 'AMET')
print('Substituição altera?\t', texto2 == texto)

# capitalize vs title:
# capitalize a primeira letra da string é capitalizada.
# title a primeira letra de cada palavra é capitalizada

# texto.strip() tira os espaços do inicio e do fim. (trailing spaces).
# similarmente, lstrip() e rstrip()

# texto.split() pega cada palavra.
# texto.split('i') divide em 3 strings, entre os Is

print(texto.split('i'))
print('-'.join(texto.split()))


# Aspas multilinha

# Contrabarra para não incluir a quebra de linha
print( """\
Eu vim para contar a história
	de um tatu que já morreu
Passando muito trabalho
	por esse mundo de Deus""")


# frase[0] = 'J' ==> erro. é imutável.
# só se frase = frase.replace('lorem', 'borem')
