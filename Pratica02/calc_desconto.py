"""
2- Calculadora de Desconto 
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

produto = "camiseta"
preco = 50.00
desconto = 20

print (f"O preço de uma {produto} é de R${preco:.2f}.")
print (f"Em uma promoção, a loja ofereceu {desconto}% de desconto.")
print (f"Assim, o valor final da camiseta ficou R${preco - (desconto/100*preco):.2f}.")