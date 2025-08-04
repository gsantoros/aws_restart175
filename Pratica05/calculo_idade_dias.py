"""
4. Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de
nascimento.
"""

import datetime

def calc_idade_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias
    
ano_nasc = int(input("Digite o ano do seu nascimento: "))

idade_em_dias = calc_idade_dias(ano_nasc)
print(f"Sua idade, em dias, aproximada é de: {idade_em_dias} dias.")