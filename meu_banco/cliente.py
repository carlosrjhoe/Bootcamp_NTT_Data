from datetime import datetime


class Cliente:
    def __init__(self, endereco: str):
        self.__endereco = endereco
        self.__contas = []

    @property
    def endereco(self):
        return self.__endereco

    def realiza_transacao(self, conta, transacao):
        conta.historico.adicionar_transacao(
            tipo=transacao.__class__.__name__,
            valor=transacao.valor,
            data_hora=datetime.now()
        )
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    @property
    def conta(self):
        return self.__contas


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: int):
        super().__init__(endereco)
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento
