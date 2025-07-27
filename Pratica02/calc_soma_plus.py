"""
5- Calculadora de Soma com Entrada do Usuário
Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 
Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.
"""

valor_a = int(input("Insira o valor de A: "))
valor_b = int(input("Inrira o valor de B: "))
valor_x = valor_a + valor_b

print(f"O valor de X é = {valor_x}.")