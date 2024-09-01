from cliente import PessoaFisica
from conta import ContaCorrente
from transacao import Deposito
from transacao import Saque


class Banco:
    def __init__(self):
        self.__usuarios = []
        self.__contas = []

    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def contas(self):
        return self.__contas

    def cadastrar_usuarios(self, nome: str, cpf: str, endereco: str, data_nascimento):
        for usuario in self.__usuarios:
            if usuario.cpf == cpf:
                print('CPF já cadastrado')
                return
        novo_usuario = PessoaFisica(endereco, cpf, nome, data_nascimento)
        self.__usuarios.append(novo_usuario)

    def cadastrar_conta_bancaria(self, cpf: str, agencia: str = "0001", limite: float = 1000.0, limite_saques: int = 3):
        for usuario in self.__usuarios:
            if usuario.cpf == cpf:
                numero_conta = len(self.__contas) + 1
                nova_conta = ContaCorrente(
                    numero_conta, agencia, usuario, limite, limite_saques
                )
                self.__contas.append(nova_conta)
                usuario.adicionar_conta(nova_conta)
                print(
                    f'Conta bancária: {numero_conta}'
                    f'Cadastrada com sucesso para o usuário: {usuario.nome}'
                )
                return
        print('Usuário não encontrado. Cadastre o usuário antes de criar uma conta.')

    def depositar(self, valor: float, numero_conta: int):
        for conta in self.__contas:
            if conta.numero == numero_conta:
                deposito = Deposito(valor)
                deposito.registrar(conta)
                return
        print('Conta não cadastrada.')

    def sacar(self, valor: float, numero_conta: int):
        for conta in self.__contas:
            if conta.numero == numero_conta:
                saque = Saque(valor)
                saque.registrar(conta)

    def visualizar_extrato(self, numero_conta: int):
        for conta in self.__contas:
            if conta.numero == numero_conta:
                conta.historico.exibir_extrato()
                print(f'Saldo atual: R${conta.exibir_saldo():.2f}')
                return
        print('Conta não cadastrada.')


def separador():
    print('#'*65)


def menu():
    print('\nEscolha uma operação')
    print('1 - Cadastrar usuário.')
    print('2 - Cadastrar conta bancária.')
    print('3 - Depósito.')
    print('4 - Sacar.')
    print('5 - Visuasilar extrato.')
    print('Q - Sair.')


def main():
    banco = Banco()

    while True:
        separador()
        menu()
        opcao = input('Digite sua operação: ').upper()

        if opcao == '1':
            nome = input('Informe seu nome: ').title()
            cpf = input('Informe seu CPF: ')
            endereco = input('Informe seu endereco: ')
            data_nascimento = input('Informe sua data de nascimento:')
            banco.cadastrar_usuarios(nome, cpf, endereco, data_nascimento)
        elif opcao == '2':
            cpf = input('Informe o CPF do usuário: ')
            banco.cadastrar_conta_bancaria(cpf)
        elif opcao == '3':
            numero_conta = int(input('Informe o número da conta: '))
            valor = float(input('Informe o valor do deposito: '))
            banco.depositar(valor, numero_conta)
        elif opcao == '4':
            numero_conta = int(input('Informe o número da conta: '))
            valor = float(input('Informe o valor do saque: '))
            banco.sacar(valor, numero_conta)
        elif opcao == '5':
            numero_conta = int(input('Informe o número da conta: '))
            banco.visualizar_extrato(numero_conta)
        elif opcao == 'Q':
            print('Saindo do sistema bancário.')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
