"""
4- Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

produto = "Cadeira Infantil"
preco_uni = 12.40
quantidade = 3

print (f"O preço de uma {produto} é R$ {preco_uni:.2f}. Comprando {quantidade} cadeiras, o preço total da compra será de R${preco_uni * quantidade:.2f}.")