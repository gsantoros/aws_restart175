"""
3- Calculadora de Média Escolar 
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

Nota 1: 7.5
Nota 2: 8.0
Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = nota1+nota2+nota3

print (f"Um aluno terminou o semestre com as seguintes notas: {nota1}, {nota2} e {nota3}.")
print (f"A média fianl deste aluno é {media / 3:.2f}")