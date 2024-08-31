from datetime import date
from datetime import datetime
from datetime import timedelta

def new_func1():
    print('#'*30)
    data = date(2024, 8, 30)
    print(date.today())
    print('#'*30)

    data_hora = datetime.today()
    print(data_hora)
    print('#'*30)

tipo_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
mascara = '%d/%m/%y %H:%M'

def new_func():
    if tipo_carro == 'P':
        data_estimativa = data_atual + timedelta(minutes=tempo_pequeno)
        print(f'O carro chegou as: {data_atual.strftime(mascara)} e ficará pronto às: {data_estimativa}')
    elif tipo_carro == 'M':
        data_estimativa = data_atual + timedelta(minutes=tempo_medio)
        print(f'O carro chegou as: {data_atual} e ficará pronto às: {data_estimativa}')
    else:
        data_estimativa = data_atual + timedelta(minutes=tempo_grande)
        print(f'O carro chegou as: {data_atual} e ficará pronto às: {data_estimativa}')

def main():
    new_func1()
    new_func()

if __name__ == '__main__':
    main()