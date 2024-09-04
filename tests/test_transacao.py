import pytest


def test_deposito_valor(deposito):
    assert deposito.valor == 1000.0


def test_deposito_data_hora(deposito):
    assert deposito.data_hora is not None


def test_deposito_registrar_saldo(conta, deposito):
    deposito.registrar(conta)
    assert conta.saldo == 1000.0


def test_deposito_registrar_historico(conta, deposito):
    deposito.registrar(conta)
    assert conta.historico.transacoes[0]['tipo'] == 'Depósito'
