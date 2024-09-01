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
