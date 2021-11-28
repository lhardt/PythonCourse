# Valor do Aluguel
# Calcular o valor do aluguel de um carro
#  com base na quilometragem rodada e no
#  número de dias rodados

dias = float(input('Digite o número de dias de aluguel:  '))
kms = float(input('Digite o número de KMs rodados:  '))

# Constantes?
valor_total = (dias * 60) + (.15 * kms)

print('O valor total do aluguel é: R$ {:.2f}'.format(valor_total))
