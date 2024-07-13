class Conta:
  def __init__(self, numero, cliente, saldo=0, agencia="0001"):
      self.numero = numero
      self.agencia = agencia
      self.cliente = cliente
      self.saldo = saldo
      self.extrato = Historico()

  def deposita(self, valor):
      self.saldo += valor
      self.extrato.transacoes.append(Deposito(data_hoje(), valor, self))

  def saca(self, valor):
      if self.saldo >= valor:
          self.saldo -= valor
          self.extrato.transacoes.append(Saque(data_hoje(), valor, self))
      else:
          print("Saldo insuficiente para saque.")

  def extrato(self):
      print(f"Extrato da conta {self.numero}:")
      for transacao in self.extrato.transacoes:
          print(transacao)

  def mostra_saldo(self):
      print(f"Saldo atual da conta {self.numero}: {self.saldo}")

  def historico(self):
      print(f"Histórico da conta {self.numero}:")
      self.extrato.imprime()

class ContaCorrente(Conta):
  def __init__(self, numero, cliente, saldo=0, agencia="0001", limite=1000, limite_saques=5):
      super().__init__(numero, cliente, saldo, agencia)
      self.limite = limite
      self.limite_saques = limite_saques

  def saca(self, valor):
      if self.saldo + self.limite >= valor:
          self.saldo -= valor
          self.extrato.transacoes.append(Saque(data_hoje(), valor, self))
      else:
          print("Saldo insuficiente e limite de crédito excedido para saque.")

class Cliente:
  def __init__(self, nome, cpf):
      self.nome = nome
      self.cpf = cpf

class PessoaFisica(Cliente):
  def __init__(self, nome, cpf, idade):
      super().__init__(nome, cpf)
      self.idade = idade

class Transacao:
  def __init__(self, data, valor, conta):
      self.data = data
      self.valor = valor
      self.conta = conta

  def __str__(self):
      return f"Data: {self.data}, Valor: {self.valor}, Conta: {self.conta.numero}"

class Saque(Transacao):
  def __init__(self, data, valor, conta):
      super().__init__(data, valor, conta)

class Deposito(Transacao):
  def __init__(self, data, valor, conta):
      super().__init__(data, valor, conta)

class Historico:
  def __init__(self):
      self.transacoes = []

  def imprime(self):
      for transacao in self.transacoes:
          print(transacao)

def data_hoje():
  import datetime
  return datetime.datetime.now()
