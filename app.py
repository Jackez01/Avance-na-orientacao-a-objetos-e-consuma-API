from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('suco de melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_lanche = Prato('Paozinho', 2.00, 'lanche com carne e queijo')
prato_lanche.aplicar_desconto()
prato_sobremesa = Sobremesa('Brigadeiro de colher', 10.00, 'Muito doce' )
prato_sobremesa.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_lanche )
restaurante_praca.adicionar_no_cardapio(prato_sobremesa)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()