"""
3- Calculadora de IMC
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite a sua altura (metros): "))

imc = peso / (altura**2)

if imc < 18.5:
    classificacao = "abaixo do peso"
elif imc < 25:
    classificacao = "no peso normal"
elif imc < 30:
    classificacao = "com sobrepeso"
else:
    classificacao = "obeso(a)"

print(f"Seu atual IMC é de: {imc:.2f}.")
print(f"E você está {classificacao}.")