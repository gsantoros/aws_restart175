"""
5- Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas
"""

A = int(input("Insira o valor de A: "))
B = int(input("Insira o valor de B: "))
C = int(input("Insira o valor de C: "))
D = int(input("Insira o valor de D: "))
diferenca = (A * B - C * D)

print(f"A diferença de A*B - C*D é igual a = {diferenca}")