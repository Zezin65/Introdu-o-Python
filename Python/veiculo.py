class Veiculo: #classe Pai
    rodas = 0
    motor = 0.0
    potencia = 0
    velocidade = 0
    marcha = 0
    nome = ""
    cor = ""
    modelo = ""

    def __init__(self, rodas, motor, potencia, 
                 velocidade, marcha, nome, cor, modelo) -> None:
        self.rodas = rodas
        self.motor = motor
        self.potencia = potencia
        self.velocidade = velocidade
        self.marcha = marcha
        self.nome = nome
        self.cor = cor
        self.modelo = modelo

    def acelerar(self):
        pass

    def freiar(self):
        pass


class Carro(Veiculo):
    portas = 0

    def __init__(self, rodas, motor, potencia, velocidade, marcha, 
                 nome, cor, modelo, portas) -> None:
        super().__init__(rodas, motor, potencia, 
                         velocidade, marcha, nome, cor, modelo)
        self.portas = portas

    def re(self):
        pass

class Moto(Veiculo):
    cilindradas = 0

    def empinar(self):
        pass