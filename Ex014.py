""""
25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. 
Analise seus comprimentos e diga se é possível formar um triângulo com essas
retas. Matematicamente, para três de cada lado deve ser menor que a soma dos outros dois
"""
primeira_reta = (input('Digite o Valor da primeira Reta: '))
segunda_reta = (input('Digite o Valor da segunda Reta: '))
terceira_reta = (input('Digite o Valor da terceira Reta: '))


try:
    float(primeira_reta)
    float(segunda_reta)
    float(terceira_reta)
    soma_dos_lados = primeira_reta + segunda_reta
    if soma_dos_lados < terceira_reta:
        print('É possivel formar um Triangulo.')
    else:
        print('Nāo é possivel formar um triangulo.')
except:
    print('Você nāo digitou o valor corretamente ')





