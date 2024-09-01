from historico import Historico
from cliente import Cliente


class Conta:
    def __init__(self, numero, agencia, cliente: Cliente):
        self.__saldo = 0.0
        self.__numero = numero
        self.__agencia = agencia
        self.__cliente = cliente
        self.__historico = Historico()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia

    @property
    def cliente(self):
        return self.__cliente

    @property
    def historico(self):
        return self.__historico

    def sacar(self, valor: float) -> bool:
        if valor > self.__saldo:
            print(f'Saldo insuficiente.')
            return False
        self.__saldo -= valor
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print(f'Valor de depósito inválido.')
            return False
        self.__saldo += valor
        return True

    def exibir_saldo(self):
        return self.__saldo


class ContaCorrente(Conta):
    def __init__(self, numero: int, agencia: str, cliente: Cliente, limite: float, limite_saques: int):
        super().__init__(numero, agencia, cliente)
        self.__limite = limite
        self.__limite_saques = limite_saques
        self.__saques_realizados = 0

    @property
    def limite_saques(self):
        return self.__limite

    @property
    def limite_saques(self):
        return self.__limite_saques

    @property
    def limite_saques_realizados(self):
        return self.__limite_saques_realizados

    def sacar(self, valor: float) -> bool:
        if self.__saques_realizados >= self.__limite_saques_realizados:
            print(f'Limite sde saques diários atingido.')
            return False
        elif valor > (self.saldo + self.__limite):
            print(f'Saldo insuficiente.')
            return False
        elif super().saque(valor):
            self.__saques_realizados += 1
            return True
        return False
