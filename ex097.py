# Crie uma função "escreva" que, a partir de uma mensagem,
# a escreva com uma linha superior e inferior, com o tamanho adequado ao texto;
# Exmplos:
#
# ========
#  PYTHON
# ========
#
# =================
#  Curso de Python
# =================

def escreva(mensagem):
	largura = 2+len(mensagem)
	print('=' * largura)
	print(f' {mensagem} ')
	print('=' * largura)


str = input('Digite uma mensagem:\n>>>\t')
print()
escreva(str)
