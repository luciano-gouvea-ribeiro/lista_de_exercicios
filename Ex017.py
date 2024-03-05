'''
 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
'''
from datetime import date
ano_atual = date.today().year
maior_de_18 = 0
menor_de_18 = 0
cont = 0

for i in range(1,8):
    cont += 1
    ano_nascimento = int(input(f'Em que ano a {cont } pessoa nasceu?'))

    if ano_atual - ano_nascimento >= 18:
        maior_de_18 += 1
    elif ano_atual - ano_nascimento <= 18:
        menor_de_18 += 1

print(f'Das 6 pessoa informadas essa é a quantidade de maiores: {maior_de_18}')
print(f'Das 6 pessoa informadas essa é a quantidade de menores: {menor_de_18}')

