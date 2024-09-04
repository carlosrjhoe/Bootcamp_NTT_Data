import pytest


def test_conta_inicial_saldo_zero(conta):
    assert conta.saldo == 0.0


def test_conta_depositar_valor_positivo(conta, deposito):
    conta.depositar(deposito.valor)
    assert conta.saldo == deposito.valor


def test_conta_depositar_valor_invalido(conta):
    resultado = conta.depositar(-100.0)
    assert resultado == False
    assert conta.saldo == 0.0


def test_conta_sacar_valor_positivo(conta, deposito):
    conta.depositar(deposito.valor)
    resultado = conta.sacar(500.0)
    assert resultado == True
    assert conta.saldo == 500.0


def test_conta_sacar_valor_insuficiente(conta, deposito):
    conta.depositar(deposito.valor)
    resultado = conta.sacar(1500.0)
    assert resultado == False
    assert conta.saldo == deposito.valor


def test_conta_sacar_valor_invalido(conta):
    resultado = conta.sacar(-100.0)
    assert resultado == False
    assert conta.saldo == 0.0
