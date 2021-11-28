# Crie um programa que leia quanto dinheiro
# alguém tem na carteira, e mostre quantos
# dólares essa pessoa pode comprar.

reais = float(input('Quantos reais? R$'))

print('Isso dá $ {:.2f}'.format( reais / 3.27 ))
