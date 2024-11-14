# main.py

from banco import Banco

# Criação de um objeto Banco
Tradesco = Banco("Sergio", "149.654.754-69", "serginhoReidelas123", "15/12/1953")

# Impressão do saldo inicial
print("Saldo inicial:", Tradesco.get_saldo())

# Definindo o saldo
Tradesco.set_saldo(200)
print("Saldo após definição:", Tradesco.get_saldo())

# Depositando dinheiro
print("Depositando R$ 100...")
Tradesco.depositar(100)
print("Saldo após depósito:", Tradesco.get_saldo())

# Sacando dinheiro
print("Sacando R$ 50...")
Tradesco.sacar(50)
print("Saldo após saque:", Tradesco.get_saldo())

# Tentativa de saque inválido
try:
    print("Tentando sacar R$ 300...")
    Tradesco.sacar(300)
except ValueError as e:
    print("Erro:", e)
