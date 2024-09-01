class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes

    def adicionar_transacao(self, transacao):
        self.__transacoes.append(transacao)

    def exibir_extrato(self):
        if not self.__transacoes:
            print(f'Nenhuma movimentação registrada.')
        for transacao in self.__transacoes:
            print(f'{transacao}')
