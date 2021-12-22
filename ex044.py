# Elabore um programa que calcula o valor
# de um produto, a partir da cond. de pgto.
# A vista (dinh, cheque): 10% a menos
# A vista no cartão: 5% de desc.
# Em até 2x no cartão: preço normal
# Mais de 2x: 20% de juros
print('Digite o preço de vitrine:')

valorBase = float(input('>>>\tR$ '))

print('Selecione a forma de pagamento:')
print('1. Dinheiro')
print('2. Cheque')
print('3. Cartão a vista')
print('4. Cartão 2x')
print('5. Cartão +3x')

selecao = int(input('>>>\t'))

switcher = {
	1: 0.9,
	2: 0.9,
	3: 0.95,
	4: 1,
	5: 1.2
}

try:
	valorFinal = valorBase * (switcher.get(selecao))
	print('O preço final será de R$ {:.2f}.'.format(valorFinal))
except Exception:
	print('Seleção Inválida.')
