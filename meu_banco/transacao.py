from abc import ABC
from abc import abstractmethod


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        if conta.depositar(self.__valor):
            conta.historico.adicionar_transacao(
                f'Depósito de R${self.__valor:.2f}'
            )


class Saque(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        if conta.sacar(self.__valor):
            conta.historico.adicionar_transacao(
                f'Saque de R${self.__valor:.2f}'
            )
