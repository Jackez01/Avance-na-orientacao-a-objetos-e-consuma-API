# serve para criar um metodo abstrato
from abc import ABC, abstractmethod

class itemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    #serve para aplicar esse metodo em todas as classes dos itens do cardapio
    @abstractmethod
    def aplicar_desconto(self):
        pass