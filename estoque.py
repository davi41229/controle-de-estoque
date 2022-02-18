class Estoque:

	def __init__(self, produto, valor, codigo):
		self.produto = produto
		self.valor = valor
		self.codigo = codigo

	def __str__(self):
		return "Produto: " + self.produto + "\nValor: " + str(self.valor) + "\nCodigo: " + str(self.codigo)
