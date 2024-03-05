'''
Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, 
que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.

'''

def somaimposto(taxaimposto, custo):
    valor_porcentagem = taxaimposto / 100
    print(f'valor da porcentagem {valor_porcentagem}')
    print()
    retorno = valor_porcentagem + custo
    print(f'soma total de custos com imposto do produto é de {retorno}')



somaimposto(150, 35)
