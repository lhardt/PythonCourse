# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, sendo R$ 0,50 por km até 200km e R$ 0,45
# para viagens mais longas.

dist = int(input('Qual é a distância da viagem?\n>>>\t'))

preco = dist * (0.45 if dist > 200 else 0.5 )

print('O preço final da passagem é {:.2f}.'.format(preco))
