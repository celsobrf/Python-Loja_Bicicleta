from Cliente import Cliente
from Loja import Loja

cliente01 = Cliente("Cliente 01")
cliente02 = Cliente("Cliente 02")
cliente03 = Cliente("Cliente 03")
loja01 = Loja("Loja 01",5,{"hora":5.00,"dia":25.00,"semana":100.00})
loja02 = Loja("Loja 02",6,{"hora":5.00,"dia":25.00,"semana":100.00})

cliente01.consultarEstoque(loja01)
cliente01.consultarEstoque(loja02)

cliente03.solicitarAluguel(loja02, 1, "semana")     # Simula locacao normal sem desconto familia
cliente03.devolverAluguel(loja02)                   # Calculo de locacao sem desconto familia

cliente01.solicitarAluguel(loja01, 3, "dia")  # Simula locacao com desconto familia

try:
    cliente02.solicitarAluguel(loja01, 3, "dia")     # Simular pedido em loja sem estoque suficiente
except Exception as e:
    print(str(e))

try:
    cliente03.solicitarAluguel(loja02, 3, "ano")     # Simular pedido em loja em modalidade invalida
except Exception as e:
    print(str(e))

cliente01.devolverAluguel(loja02)               # Simular devolucao em loja diferente da que foi locada

cliente01.consultarEstoque(loja01)
cliente01.consultarEstoque(loja02)
cliente01.devolverAluguel(loja01)               # Simula devolucao e conta com desconto familia