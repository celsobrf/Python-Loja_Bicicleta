from datetime import datetime
from Loja import Loja

class Cliente(object):
  
  def __init__(self, nome: str):
    self.nome: str = nome
    self.statusLocacao: bool = False #Status de locação True = Em Locação e False = Sem locação
    self.lojaLocada: str = None
    self.dataLocacao: datetime = None
    self.quantidadeLocada: int = 0
    self.modo: str = None
    self.registroLog(nome,"__init__","Criado objeto")

  def __repr__(self) -> str:
    return f"Cliente | Nome : {self.nome} | Em Locação : {self.statusLocacao}"

  def registroLog(self, nome: str, metodoClasse: str, status: str):
    print(f"Classe: Cliente - Objeto: {nome} - Metodo: {metodoClasse} - Status: {status} - Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

  def consultarEstoque(self, loja: Loja) -> int:
    self.registroLog(self.nome,"consultarEstoque",f"Cliente solicita estoque da loja {loja.nome}")
    if not isinstance(loja, Loja):
      self.registroLog(self.nome,"consultarEstoque",f"Tipo de Objeto nao e Loja")
      raise TypeError(f"ERRO - Cliente - consultarEstoque - O parâmetro é do tipo: [{type(loja)}]")
    return loja.consultarEstoque()

  def solicitarAluguel(self, loja: Loja, quantidade: int, modo: str):
    self.registroLog(self.nome,"solicitarAluguel",f"Cliente solicita aluguel de {quantidade} bicicletas em modo {modo} na loja {loja.nome}")
    if not isinstance(loja, Loja):
      self.registroLog(self.nome,"solicitarAluguel",f"Tipo de Objeto nao e Loja")
      raise TypeError(f"ERRO - Cliente - consultarEstoque - O parâmetro é do tipo: [{type(loja)}]")
    if not self.statusLocacao:
      self.statusLocacao = True
      self.lojaLocada = loja.nome
      self.dataLocacao = datetime.now()
      self.quantidadeLocada = quantidade
      self.modo = modo
      loja.solicitarAluguel(quantidade, modo)
    else:
      self.registroLog(self.nome,"solicitarAluguel",f"Cliente possui bicicleta alugada no momento.")
  
  def devolverAluguel(self, loja: Loja) -> float:
    self.registroLog(self.nome,"devolverAluguel",f"Cliente solicita devolução de aluguel para a loja {loja.nome}")
    if not isinstance(loja, Loja):
      self.registroLog(self.nome,"devolverAluguel",f"Tipo de Objeto nao e Loja")
      raise TypeError(f"ERRO - Cliente - consultarEstoque - O parâmetro é do tipo: [{type(loja)}]")
    if self.statusLocacao and loja.nome == self.lojaLocada:
      self.registroLog(self.nome,"devolverAluguel",f"Verifica se cliente {self.nome} possui bicicleta alugada e informa aluguel realizado em {self.dataLocacao}")
      loja.devolverAluguel(self.quantidadeLocada)
      valor_a_pagar = self.calculaConta(loja)
      self.statusLocacao = False
      self.lojaLocada = None
      self.quantidadeLocada = 0
      self.dataLocacao = None
      self.modo = None
      self.registroLog(self.nome,"devolverAluguel",f"Cliente recebe valor do aluguel da {loja.nome} no valor de R$ {valor_a_pagar:.2f}")
    else:
      valor_a_pagar = 0.0
      self.registroLog(self.nome,"devolverAluguel",f"Cliente nao possui bicicleta alugada na loja {loja.nome}")
    return valor_a_pagar

  def calculaConta(self, loja: Loja) -> float:
    self.registroLog(self.nome,"calculaConta",f"Cliente solicita Calculo de Conta")
    if not isinstance(loja, Loja):
      self.registroLog(self.nome,"calculaConta",f"Tipo de Objeto nao e Loja")
      raise TypeError(f"ERRO - Cliente - consultarEstoque - O parâmetro é do tipo: [{type(loja)}]")
    else:
      return loja.calculaConta(self.dataLocacao, self.modo, self.quantidadeLocada)