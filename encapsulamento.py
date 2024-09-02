class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def sacar(self, valor):
        self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor

    def extrato(self):
        return self._saldo


if __name__ == '__main__':
    conta = Conta(100)
    print(conta._saldo)
