from abc import ABC
from abc import abstractmethod
from datetime import datetime


class Transacao(ABC):
    def __init__(self, valor: float):
        self.__valor = valor
        self.data_hora = datetime.now()

    @property
    def valor(self):
        return self.__valor

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        super().__init__(valor)

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(
                tipo='Depósito',
                valor=self.valor,
                data_hora=self.data_hora
            )


class Saque(Transacao):
    def __init__(self, valor: float):
        super().__init__(valor)

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(
                tipo='Saque',
                valor=self.valor,
                data_hora=self.data_hora
            )
