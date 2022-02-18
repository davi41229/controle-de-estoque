#Controle de Estoque loja de roupas
#3 tipos de produtos, valores, quantidaddes.
#comprar,vender, saldo do estoque.


from estoque import Estoque
from camisa import Camisa
from calsa import Calsa
from sapato import Sapato

#produto 1 - camisas

estoque1 = Estoque('camisa', 199.99, '010')

print("Estoque")
print("--------")
print(estoque1)

camisa_azul = Camisa(estoque1, 50, 100)

print("\nEntrada")
print("--------")

camisa_azul.comprar(150)

print(camisa_azul.consulta_estoque())


print("\nsaida")
print("--------")

camisa_azul.vender(250)

print(camisa_azul.consulta_estoque())


# produto 2 - calsas

print("--------")
estoque2 = Estoque('calsa', 99.99, '005')

print("Estoque")
print("--------")
print(estoque2)

calsa_jeans = Calsa(estoque2, 20, 100)

print("\nEntrada")
print("--------")

calsa_jeans.comprar(50)

print(calsa_jeans.consulta_estoque())

print("\nsaida")
print("--------")

calsa_jeans.vender(50)

print(calsa_jeans.consulta_estoque())

#produto 3 - sapatos

print("--------")
estoque3 = Estoque('sapato', 69.99, '003')

print("Estoque")
print("--------")
print(estoque3)

sapato_social = Sapato(estoque3, 30, 10)

print("\nEntrada")
print("--------")

sapato_social.comprar(20)

print(sapato_social.consulta_estoque())

print("\nsaida")
print("--------")

sapato_social.vender(75)

print(sapato_social.consulta_estoque())
