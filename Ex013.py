'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área
'''

class Quadrado:
    def __init__(self,tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_do_lado(self, novo_tamanho_lado):
        retorno = self.tamanho_lado = novo_tamanho_lado
        return retorno
    
    def retornar_valor_lado(self):
        print(self.tamanho_lado)

    def calcular_area(self,comprimento):
     area =  self.tamanho_lado * comprimento
     print(area)
    
q1 = Quadrado(2)
print(q1.tamanho_lado)
q1.mudar_valor_do_lado(15)
print(q1.tamanho_lado)
q1.retornar_valor_lado()
q1.calcular_area(3)