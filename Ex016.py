'''
050: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''

soma_dos_pares = 0
for i in range(1,7):
    numero = int(input('Digite um valor numerico: '))
    if numero % 2 == 0:
        soma_dos_pares += numero

print(f'A soma dos Numeros pares é {soma_dos_pares}')

