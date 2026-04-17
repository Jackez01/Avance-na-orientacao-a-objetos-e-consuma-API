# 3. Crie uma nova classe chamada Carro que herda da classe Veiculo.
from metodos_especiais_e_atributos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca,  modelo)
        self.cor = cor

    def ligar(self):
        print(f'Seu carro está ligado {self.modelo}')

    def __str__(self):
        return f'{super().__str__()} | cor: {self.cor}'

# 4. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e 
# atribua o atributo específico cor à classe filha.