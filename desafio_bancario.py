usuarios = []
contas = []
saldo = 0
extrato = []
saques_realizados = 0
LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_SAQUE = 500


def cadastrar_usuarios(nome: str, cpf: str) -> None:
    """Esta função registra um novo cliente, verificando se o CPF já está cadastrado. Se não estiver, adiciona o cliente à lista de usuários."""
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('CPF já cadastrado.')
        else:
            return
    usuario = {'nome': nome, 'cpf': cpf}
    usuarios.append(usuario)
    print(f'Usuário {nome} cadastrado comsucesso.')


def cadastrar_conta_bancaria(cpf: str) -> None:
    """Esta função cria uma conta bancária para o cliente, associando a conta ao CPF do usuário e inicializando o saldo e o extrato."""
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            numero_conta = len(contas) + 1
            conta = {'numero_conta': numero_conta,
                     'cpf': cpf, 'saldo': 0, 'extrato': []}
            contas.append(conta)
            print(
                f'Conta bancária {numero_conta} '
                f'cadastrada com sucesso para o usuário {usuario}')
            return
    print('Usuário não encontrado. Cadastre o usuário antes de criar uma conta.')


def depositar(valor: float, numero_conta: int) -> None:
    """Permite adicionar um valor ao saldo de uma conta específica. O valor deve ser positivo e a conta deve existir."""
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            if valor > 0:
                conta['saldo'] += valor
                conta['extrato'].append(
                    f'Depósito de R${valor:.2f} realizado com sucesso na conta: {numero_conta}.')
            else:
                print(f'Valor de depósito inválido.')
            return
    print('Conta não cadastrada.')


def sacar(valor: float, numero_conta: int) -> None:
    """Permite retirar um valor do saldo de uma conta específica. A função verifica limites diários de saques, o valor máximo de saque, e se há saldo suficiente."""
    global saques_realizados
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            if saques_realizados >= LIMITE_SAQUES_DIARIOS:
                print(f'O limite desaques diários atigindo.')
            elif valor > LIMITE_VALOR_SAQUE:
                print(f'O valor maximo para saque é de: '
                      f'R${LIMITE_VALOR_SAQUE:.2f}.')
            elif valor > conta['saldo']:
                print('Saldo insuficiente.')
            elif valor < 0:
                print('Valor de saque inválido.')
            else:
                conta['saldo'] -= valor
                saques_realizados += 1
                conta['extrato'].append(f'Saque: R${valor:.2f}')
                print(f'Saque de R${valor:.2f} '
                      f'realizado com sucesso na conta: {numero_conta}.')
            return
    print('Conta não cadastrada.')


def visualizar_extrato(numero_conta: int):
    """Mostra todas as movimentações (depósitos e saques) e o saldo atual de uma conta específica."""
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            texto = ' Movimentação '
            print(f'{texto.center(30, "#")}')
            if not conta['extrato']:
                print(f'Não tem movimentação.')
            else:
                for movimento in conta['extrato']:
                    print(f'{movimento}')
            print(f'Saldo atual: R${conta["saldo"]:.2f}')
            return
    print('Conta não cadastrada.')


def menu():
    print('\nEscolha uma operação:')
    print('1 - Cadastrar usuário.')
    print('2 - Cadastrar conta bancária.')
    print('3 - Deposito.')
    print('4 - Sacar.')
    print('5 - Visuasilar extrato.')
    print('Q - Sair.')


def main():
    while True:
        menu()
        opcao = input('Digite sua operação: ').upper()

        if opcao == '1':
            nome = input('Informe seu nome: ').title()
            cpf = input('Informe seu CPF: ')
            cadastrar_usuarios(nome, cpf)
        elif opcao == '2':
            cpf = input('Informe o CPF do usuário: ')
            cadastrar_conta_bancaria(cpf)
        elif opcao == '3':
            numero_conta = int(input('Informe o número da conta: '))
            valor = float(input('Informe o valor do deposito: '))
            depositar(valor, numero_conta)
        elif opcao == '4':
            numero_conta = int(input('Informe o número da conta: '))
            valor = float(input('Informe o valor do saque: '))
            sacar(valor, numero_conta)
        elif opcao == '5':
            numero_conta = int(input('Informe o número da conta: '))
            visualizar_extrato(numero_conta)
        elif opcao == 'Q':
            break


if __name__ == '__main__':
    main()
