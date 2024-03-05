"""
68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”.
 No final, mostre na tela:
a) Quantas mulheres foram cadastradas 
b) Quantos homens pesam mais de 100Kg 
c) A média de peso entre as mulheres 
d) O maior peso entre os homens
"""
mulheres_cadastradas = 0
homens_mais_de_100kg = 0
peso_das_mulheres = 0
media_de_peso_mulheres = 0
maior_peso_homens = 0


        
for pessoa in range(0,8):
    sexo_da_pessoa = input('Digite a sua opçāo sexual: [M/F]').upper()
    peso_das_pessoas = float(input('Digite o seu peso atual: '))

    if sexo_da_pessoa == 'F':
        mulheres_cadastradas += 1
        peso_das_mulheres += peso_das_pessoas
        media_de_peso_mulheres = peso_das_mulheres / mulheres_cadastradas
    elif sexo_da_pessoa == 'M' and peso_das_pessoas >= 100:
        homens_mais_de_100kg += 1
        if peso_das_pessoas >= maior_peso_homens:
            maior_peso_homens = peso_das_pessoas
    
print()
    
print(f'Total de mulheres cadastradas: {mulheres_cadastradas} ')    
print(f'Total de homens com mais de 100kg: {homens_mais_de_100kg} ')
print(f'media do peso das mulheres: {media_de_peso_mulheres} ')
print(f'O maior peso entre os homens é {maior_peso_homens}')




