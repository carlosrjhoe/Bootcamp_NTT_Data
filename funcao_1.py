def add(a: int, b: int) -> None:
    return a + b

def subtract(a: int, b: int) -> None:
    return a - b

def display_result(a: int, b: int, funcao: int) -> None:
    result = funcao(a, b)
    print(f'O resultado da operação é de = {result}')


if __name__ == '__main__':
    a, b = 12, 8
    display_result(a, b, add)
    display_result(a, b, subtract)
    