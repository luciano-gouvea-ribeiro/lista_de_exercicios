'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor,circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocarCor(self, cor):
        retorno = self.cor = cor
        return retorno
    
    def mostrarCor(self):
        print(self.cor)

b1 = Bola('rosa', 9.0, 'plastico')

b1.trocarCor('roxo')
b1.mostrarCor()
print(b1.cor)
print(b1.circunferencia)
print(b1.material)

