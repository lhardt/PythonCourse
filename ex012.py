# Crie um programa em que o usuário dê o preço
# de um produto, e o programa mostre o valor
# dele em liquidação, com 5 % de desconto.

original = float(input('Preço original: '))

print('O preço descontado é : R$ {:.2f}'.format( 0.95 * original))
