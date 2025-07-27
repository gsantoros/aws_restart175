"""
1- Conversor de Moeda 
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

v_real = 100.00
v_dolar = 5.60
v_euro = 6.60

print (f"Uma pessoa prentende converter {v_real:.2f} reais em dólares ou euros.")
print (f"Na contação atual o valor do dólar é de R${v_dolar:.2f}, e do euro R${v_euro:.2f}.")
print (f"Estão está pessoa terá, repectivamente, U${v_real/v_dolar:.2f} ou €{v_real/v_euro:.2f}.")