''' 
Leia 3 valores reais (A, B e C) e verifique se 
eles formam ou não um triângulo. Em caso positivo, 
calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B
 como base e C como altura, mostrando a mensagem

Area = XX.X
'''


try:
    a = float(input('Digite o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    c = float(input('Digite o terceiro valor: '))


    if a + b > c:
        
        perimetro = a + b + c
        print(f'o Perimetro do Tiangulo é {perimetro}')
    else:
        area = (a + b) * c / 2
        print(f'a Area do Trapezio é {area}')

except:
    print('Você nāo digitou corretamente os valores..')



