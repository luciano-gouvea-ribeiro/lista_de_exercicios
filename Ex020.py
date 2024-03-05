''''
66) Escreva um programa que leia um número qualquer e mostre a tabuada desse número, usando a estrutura “para”.
Ex: Digite um valor: 5
5x1=5
5 x 2 = 10
5 x 3 = 15 ...

'''
numero = int(input('Digite um numero: '))
for i in range(11):
    print(f'{numero} x {i} =  {numero*i}')