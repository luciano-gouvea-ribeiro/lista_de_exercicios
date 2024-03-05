'''
Exercicio 038
 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
primeiro_numero = int(input('Digite o primeiro valor: '))
segundo_numero = int(input('Digite o segundo valor: '))

if primeiro_numero == segundo_numero:
    print('Os dois Numeros são Iguais')
elif segundo_numero > primeiro_numero:
    print(f'O segundo numero é maior que o primeiro')
elif primeiro_numero > segundo_numero:
    print(f'O primeiro numero é maior que o segundo')
