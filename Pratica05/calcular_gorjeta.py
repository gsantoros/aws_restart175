"""
1. Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)
while True:
    try:
        valor_conta = float(input("Insira o valor total da conta: "))
        porcentagem = float(input("Insira a porcentagem da gorjeta: "))
        if valor_conta < 0 or porcentagem < 0:
            print("Erro: valores negativos não são permitidos.\n")
            continue

        valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
        print(f"\nValor da gorjeta: R${valor_gorjeta:.2f}")
        print(f"Total a pagar com gorgeta: R$ {valor_conta + valor_gorjeta:.2f}")
    
    except ValueError:
        break