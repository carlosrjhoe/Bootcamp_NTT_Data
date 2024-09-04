import pytest
from datetime import datetime


def test_historico_adicionar_transacao(historico):
    data_hora = datetime.now()
    historico.adicionar_transacao(
        tipo="Depósito", valor=100.0, data_hora=data_hora)
    transacao = historico.transacoes[0]
    assert transacao["tipo"] == "Depósito"


def test_historico_adicionar_transacao_valor(historico):
    data_hora = datetime.now()
    historico.adicionar_transacao(
        tipo="Saque", valor=50.0, data_hora=data_hora)
    transacao = historico.transacoes[0]
    assert transacao["valor"] == 50.0


def test_historico_adicionar_transacao_data_hora(historico):
    data_hora = datetime.now()
    historico.adicionar_transacao(
        tipo="Depósito", valor=100.0, data_hora=data_hora)
    transacao = historico.transacoes[0]
    assert transacao["data_hora"] == data_hora.strftime('%d/%m/%Y %H:%M:%S')


def test_historico_exibir_extrato_sem_transacoes(historico, capsys):
    historico.exibir_extrato()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Nenhuma movimentação registrada."
