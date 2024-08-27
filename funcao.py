import random

def display_message_1() -> None:
    print(f'Olá mundo')

def display_message_2(name: str) -> None:
    print(f'welcome {name}')

def display_message_3(name: str = 'Mayara') -> None:
    print(f'welcome {name}')

def calculate_total(numbers: list) -> None:
    return sum(numbers)

def returns_predecessor_successor(numbers: int) -> None:
    chosen_number = random.choice(numbers)
    predecessor = chosen_number - 1
    successor = chosen_number + 1
    return predecessor, successor

if __name__ == '__main__':
    name = 'Carlos'
    numbers = [1, 2, 3, 4, 5]
    display_message_1()
    display_message_2(name)
    display_message_3('Neto')
    print(f'{calculate_total(numbers)}')
    print(f'{returns_predecessor_successor(numbers)}')
    