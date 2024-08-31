def calcular_imposto(salario: float) -> float:
    aliquota = 0
    if salario > 0 and salario < 1100.00:
        aliquota = 0.05
    elif salario > 1100.01 and salario < 2500.00:
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario


def main():
    salario = float(input())
    beneficio = float(input())
    valor_imposto = calcular_imposto(salario)
    saida = salario - valor_imposto + beneficio
    print(f'{saida:.2f}')


if __name__ == '__main__':
    main()
