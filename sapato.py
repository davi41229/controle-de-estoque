class Sapato:

	def __init__(self, estoque, quantidade, limite):
		self.estoque = estoque
		self.quantidade = quantidade
		self.limite = limite

	def comprar(self, compra, ):
		if compra > 0:
			self.quantidade += compra
			print("Foi comprado:", compra)
		
		else:
			print("Estoque Cheio!")

	def consulta_estoque(self):
		return self.quantidade

	def vender(self, venda):
		if self.quantidade - venda < 0:
			print("estoque insuficiente para:", venda)
		else:
			self.quantidade -= venda
			print("Foi vendido:", venda)
