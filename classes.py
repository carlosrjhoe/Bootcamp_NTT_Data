class Bicicleta:
    def __init__(self, modelo: str, cor: str, ano: int, valor: float):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    def __str__(self) -> str:
        texto = (
            f'{__class__.__name__}: Modelo: {self.modelo}, '
            f'Cor: {self.cor}, Ano: {self.ano}, R${self.valor:.3f}'
        )
        return texto

    def buzinar(self):
        print('plim plim...')

    def parar(self):
        print('Biscicleta parada')

    def correr(self):
        print('Vrummmmmmmm')


if __name__ == '__main__':
    caloi = Bicicleta('caloi', 'vermelha', 2000, 1.500)
    print(caloi)
    caloi.buzinar()
    caloi.parar()
    caloi.correr()
