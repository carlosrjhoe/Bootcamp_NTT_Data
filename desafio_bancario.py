saldo = 0
extrato = []
saques_realizados = 0
LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_SAQUE = 500

def depositar(valor: float) -> None:
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R${valor:.2f}')
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')
    else:
        print(f'Valor de depósito inválido.')

def sacar(valor: float) -> None:
    global saldo, saques_realizados
    if saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print(f'O limite desaques diários atigindo.')
    elif valor > LIMITE_VALOR_SAQUE:
        print(f'O valor maximo para saque é de R${LIMITE_VALOR_SAQUE:.3f}.')
    elif valor > saldo:
        print('Saldo insuficiente.')
    elif valor < 0:
        print('Valor de saque inválido.')
    else:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f'Saque: R${valor:.2f}')
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
        
def visualizar_extrato():
    texto = ' Movimentação '
    print(f'{texto.center(30, "#")}')
    if not extrato:
        print(f'Não tem movimentação.')
    else:
        for movimento in extrato:
            print(f'{movimento}')
    print(f'Saldo atual: R${saldo:.2f}')

def menu():
    print('\nEscolha uma operação:')
    print('D - Depositar.')
    print('S - Sacar.')
    print('E - Extrato.')
    print('Q - Sair.')

def main():
    while True:
        menu()
        opcao = input('Digite sua operação: ').upper()

        if opcao == 'D':
            valor = float(input('Informe o valor de deposito: '))
            depositar(valor)
        elif opcao == 'S':
            valor = float(input('Informe o valor do saque: '))
            sacar(valor)
        elif opcao == 'E':
            visualizar_extrato()
        elif opcao == 'Q':
            break
            
if __name__ == '__main__':
   main()