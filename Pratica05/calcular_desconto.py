"""
3. Crie um programa que receba o preço original de um produto e um percentual de
desconto, realizando o cálculo do preço final após a aplicação do desconto.

Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada
esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10a0
"""
def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

preco_real = float(input("Informe o preço de um produto: "))
desconto = float(input("Informe o percentual de desconto: "))

preco_descontado = calcular_desconto(preco_real, desconto)
print (f"O valor final do produto, com {desconto}% de desconto, será de: R${preco_descontado:.2f}.")