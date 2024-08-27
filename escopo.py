salary = 3.500

def bonus_salary(bonus: float) -> None:
    global salary
    salary += bonus
    return salary

def func(*args, **kwargs):
    print(f'{args} - {kwargs}')

if __name__ == '__main__':
    bonus = 0.500
    print(f'R$ {bonus_salary(bonus):.3f}')
    func("python", 2022, curso="dio")
    