from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('suco de melancia', 5.00, 'grande')
prato_lanche = Prato('Paozinho', 2.00, 'lanche com carne e queijo')


def main():
    print(bebida_suco)
    print(prato_lanche)

if __name__ == '__main__':
    main()