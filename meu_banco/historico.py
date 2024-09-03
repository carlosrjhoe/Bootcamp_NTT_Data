from datetime import datetime


class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes

    def adicionar_transacao(self, tipo: str, valor: float, data_hora: datetime):
        transacao_info = {
            'tipo': tipo,
            'valor': valor,
            'data_hora': data_hora.strftime('%d/%m/%Y %H:%M:%S')
        }
        self.__transacoes.append(transacao_info)

    def exibir_extrato(self):
        if not self.__transacoes:
            print(f'Nenhuma movimentação registrada.')
        for transacao in self.__transacoes:
            print(
                f'{transacao["tipo"]} de R$'
                f'{transacao["valor"]:.2f} em {transacao["data_hora"]}'
            )
            print('-' * 60)
