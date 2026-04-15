# 7. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# 8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. 
# Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade
# de portas e tipos.
from Projeto_veiculos.carro import Carro
from Projeto_veiculos.moto import Moto

carro1 = Carro('Peugeot', 'esportivo', 4)
carro2 = Carro('Sentra', 'esportivo', 4)
carro3 = Carro('Corsa', 'esportivo', 2)

moto1 = Moto('Kawasaki', 'Ninja', 'Esportiva')
moto2 = Moto()
moto3 = Moto()
# 9. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.