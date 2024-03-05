''' 
Python 004: Faça um programa que leia algo pelo teclado e mostre 
na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

palavra = input('Digite uma palavra para esse computador: ')
print('O tipo primitivo desse valor é', type(palavra))
print('Só tem Espaços? ', palavra.isspace())