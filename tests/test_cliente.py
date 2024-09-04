import pytest


def test_cliente_adicionar_conta_tamanho(cliente, conta):
    cliente.adicionar_conta(conta)
    assert len(cliente.conta) == 1


def test_cliente_adicionar_conta_numero(cliente, conta):
    cliente.adicionar_conta(conta)
    assert cliente.conta[0].numero == 1


def test_cliente_realiza_transacao_deposito(cliente, conta, deposito):
    cliente.adicionar_conta(conta)
    cliente.realiza_transacao(conta, deposito)
    assert conta.saldo == 1000.0  # O valor depositado deve ser refletido no saldo


def test_cliente_realiza_transacao_saque(cliente, conta, deposito, saque):
    cliente.adicionar_conta(conta)
    cliente.realiza_transacao(conta, deposito)  # Deposita antes do saque
    cliente.realiza_transacao(conta, saque)  # Realiza o saque
    assert conta.saldo == 500.0  # O saldo deve ser o valor inicial menos o saque
