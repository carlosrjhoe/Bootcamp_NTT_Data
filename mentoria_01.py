class Carro:
    def __init__(self, marca, qnt_portas: int, cor, data_fabricacao: int):
        print('Criando um carro novo...')
        self._marca = marca
        self.qnt_portas: int = qnt_portas
        self.cor = cor
        self.__data_fabricacao = data_fabricacao

    def __repr__(self) -> str:
        return f'{self._marca}, Quantidade de portas: {self.qnt_portas}, cor: {self.cor}, {self.__data_fabricacao}'


class CarroEsportivo(Carro):
    print('Criando carro esportivo...')
    def __init__(self, marca, qnt_portas: int, cor, data_fabricacao: int, velocidade: int):
        super().__init__(marca, qnt_portas, cor, data_fabricacao)
        self.velocidade = velocidade
        
    def __repr__(self) -> str:
        return f'{super().__repr__()}, Velocidade: {self.velocidade}Km/h'


if __name__ == '__main__':
    carro_01 = Carro('Fiat Argo', 4, 'Cinza', 2000)
    print(carro_01)
    carro_02 = Carro('Renault clio', 4, 'Prata', 2024)
    print(carro_02)
    carro_03 = CarroEsportivo('Mitsubsh', 2, 'vermolho', 2023, 340)
    print(carro_03)
