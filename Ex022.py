'''
069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
 o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
maiores_de_18 = 0
homens_cadastrados = 0
mulheres_com_menos_de_20anos = 0
menu = '''
----------------------
  CADASTRE UMA PESSOA 
----------------------
'''
while True:
    print(menu)
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'Mf':
        sexo = input('Sexo: [M/F]').strip().upper()[0]
    sair = ' '
    while sair not in 'SN':
        sair = input('Quer Continuar? [S / N]').strip().upper()[0]
    if sair == 'N':
        break  

    if idade >= 18 :
        maiores_de_18 += 1
    if sexo == 'm':
        homens_cadastrados += 1
    if idade < 20 and sexo == 'f':
        mulheres_com_menos_de_20anos += 1
    
print(f'Essa é a quantidade: {maiores_de_18} de pessoas maiores de 18 anos.')
print(f'Essa é a quantidade de Homens Cadastrados: {homens_cadastrados}')
print(f'Mulheres cadastradas com menos de 20 anos {mulheres_com_menos_de_20anos}')
