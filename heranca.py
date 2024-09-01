class Veiculo:
    def __init__(self, modelo: str, cor: str, placa: int, numero_rodas: int) -> None:
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def __str__(self) -> str:
        texto = (
            f'{__class__.__name__}: Modelo: {self.modelo}, '
            f'Cor: {self.cor}, Ano: '
            f'{self.placa}, Qtd de rodas: {self.numero_rodas}'
        )
        return texto

    def ligar_motor(self):
        print('Ligando motor.')


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, modelo: str, cor: str, placa: int, numero_rodas: int, carregado: bool) -> None:
        super().__init__(modelo, cor, placa, numero_rodas)
        self.carregado: bool = False

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} estou carregado')


if __name__ == '__main__':
    veiculo_01 = Motocicleta('tornado', 'Preta', 'abc-1234', 2)
    print(veiculo_01)
    veiculo_01.ligar_motor()

    veiculo_02 = Caminhao('Volvo FH-540', 'branca', 'klm-6130', 6, True)
    print(veiculo_02)
    veiculo_02.ligar_motor()
    veiculo_02.esta_carregado()
