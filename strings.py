def menu(texto: str) -> None:
    print(f'Caixa alta = {texto.upper()}')
    print(f'Retirar espaço em branco = {texto.strip()}')
    print(f'Retirar espaço em branco da esquerda = {texto.lstrip()}')
    print(f'Retirar espaço em branco da direita = {texto.rstrip()}')

    print(f'{texto.center(20, "-")}')

    print(f'{"-".join(texto)}')

if __name__ == '__main__':
    nome = 'Carlos Roberto'
    menu(nome)