# Calculadora de consumo médio de combustível
"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

distancia_percorida = 300   # Em Kms
combustivel_gasto = 25      # Em Litros

consumo_medio = distancia_percorida / combustivel_gasto

print("Dados da Viagem")
print(f"Distancia percorrida: {distancia_percorida} Km")
print(f"Combustível gasto: {combustivel_gasto} L")
print(f"Consumo médio de combustível: {consumo_medio:.2f} L/Km")