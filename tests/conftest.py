from meu_banco.historico import Historico
from meu_banco.transacao import Saque, Deposito
from meu_banco.banco import Banco
from meu_banco.conta import ContaCorrente
from meu_banco.cliente import PessoaFisica
import sys
import os
import pytest

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def banco():
    return Banco()


@pytest.fixture
def cliente():
    return PessoaFisica(nome="Carlos Roberto", cpf="12345678900", endereco="Rua A, 123", data_nascimento="03/11/1985")


@pytest.fixture
def conta(cliente):
    return ContaCorrente(numero=1, agencia="0001", cliente=cliente, limite=1000.0, limite_saques=3)


@pytest.fixture
def deposito():
    return Deposito(valor=1000.0)


@pytest.fixture
def saque():
    return Saque(valor=500.0)


@pytest.fixture
def historico():
    return Historico()
