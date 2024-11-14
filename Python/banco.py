# banco.py

class Banco:
    def __init__(self, nome: str, cpf: str, senha: str, data: str) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__data = data
        self.__saldo = 0.0
    
    # Métodos de acesso (Getters)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_cpf(self) -> str:
        return self.__cpf
    
    def get_senha(self) -> str:
        return self.__senha
    
    def get_data(self) -> str:
        return self.__data
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    # Métodos de modificação (Setters)
    
    def set_saldo(self, valor: float) -> None:
        if valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError("O saldo não pode ser negativo.")
    
    # Métodos adicionais
    
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor: float) -> None:
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            raise ValueError("Valor do saque inválido ou saldo insuficiente.")
