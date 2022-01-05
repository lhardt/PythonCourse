# Crie uma tupla com os 20 primeiros colocados
# do Brasileirão. Dê 4 opções ao usuário:
# a) Apenas os 5 primeiros
# b) Mostre os 4 últimos
# c) Uma lista de times, em ordem
# d) Em que posição está o Palmeiras
times = ('Atlético', 'Flamengo', 'Palmeiras', 'Fortaleza',
		 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
		 'Atlético-GO', 'Santos', 'Ceará', 'Inter', 'São Paulo',
		 'Athlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia',
		 'Sport', 'Chape')

print('*'*15)
print('Os 5 primeiros times são: ')
for i in range(5):
	print(f'\t{times[i]}')
# ou print(times[0:5])

print('*'*15)
print('Os 4 últimos são:')
for i in range(-4,0,1):
	print(f'\t{times[i]}')
# Ou print(times[-4:])

print('*'*15)
print('Em ordem alfabética, são: ')
for time in sorted(times):
	print(f'\t{time}')
# Ou print(sorted(times))
