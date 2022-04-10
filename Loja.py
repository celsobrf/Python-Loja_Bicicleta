from datetime import datetime
from datetime import timedelta

class Loja(object):
  
  segundos_por_modo = {"hora":3600,"dia":86400,"semana":604800}

  def __init__ (self, nome: str, estoque: int, modos_valores: dict):
    self.nome: str = nome
    self._estoque: int = estoque
    self.modos_valores: dict = modos_valores #Dicionários com a chave descrevendo modo e o valor daquela modalidade
    self.registroLog(nome,"__init__","Criado objeto")

  @property
  def estoque(self) -> int:
    return self._estoque

  def registroLog(self, nome: str, metodoClasse: str, status: str):
    print(f"Classe: Loja - Objeto: {nome} - Metodo: {metodoClasse} - Status: {status} - Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

  def consultarEstoque(self) -> int:
    self.registroLog(self.nome,"consultarEstoque",f"Foi informado o estoque de {self._estoque} bicicletas")
    return self._estoque
  
  def solicitarAluguel(self, quantidade: int, modo: str) -> int:
    self.registroLog(self.nome,"solicitarAluguel",f"Loja recebe o pedido")

    if modo not in self.modos_valores.keys():
      self.registroLog(self.nome,"solicitarAluguel",f"Modo informado Inválido")
      raise SystemError("ERRO - Loja - solicitarAluguel -  Modo Inválido")

    if quantidade > self._estoque:
      self.registroLog(self.nome,"solicitarAluguel",f"Quantidade indisponível")
      raise SystemError("ERRO - Loja - solicitarAluguel -  Quantidade indisponível")

    self._estoque -= quantidade
    self.registroLog(self.nome,"solicitarAluguel",f"Loja registra aluguel de {quantidade} bicicletas ficando com estoque de {self._estoque}")
    return self.estoque

  def devolverAluguel(self, quantidadeLocada: int) -> int:
    self.registroLog(self.nome,"devolverAluguel",f"Loja recebe solicitação de devolução do cliente")
    self._estoque += quantidadeLocada
    self.registroLog(self.nome,"devolverAluguel",f"Loja registra devolução de {quantidadeLocada} bicicletas ficando com estoque de {self._estoque}")
    return self._estoque

  def calculaConta(self, dataLocacao, modo: str, quantidadeLocada: int) -> float:
    self.registroLog(self.nome,"calculaConta",f"Loja realiza calculo de conta do cliente")
    datahoraAtual = datetime.now() + timedelta(days=7)  # Simula devolução 7 dias depois
    tempo = (datahoraAtual - dataLocacao).total_seconds()/Loja.segundos_por_modo[modo]
    desconto = 0 if quantidadeLocada < 3 else 0.3
    if desconto != 0:
      self.registroLog(self.nome,"calculaConta",f"Desconto aplicado de {desconto:.0%} por ter alugado apartir de 3 bicicletas.")
    valor_a_pagar = self.modos_valores[modo]*tempo*quantidadeLocada*(1-desconto)
    self.registroLog(self.nome,"calculaConta",f"Loja informa ao cliente o valor R$ {valor_a_pagar:.2f} pois o mesmo ficou por {tempo:.2f} {modo}s.")
    return valor_a_pagar