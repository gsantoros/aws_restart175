"""
4. Crie um programa que solicite ao usuário que insira números inteiros.
O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir
a quantidade de números pares e ímpares inseridos.
"""

def analisador_numero():

    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou digite 'fim' para encerrar:) ")

        if entrada.lower() == "fim":
            print("Programa encerrado.")
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é par.")
                pares += 1
            else:
                print(f"O número {numero} é impar.")
                impares += 1
        except ValueError:
            print("Erro encontrado. Por favor, digite apenas números inteiros.")

print("\nResultado Final")
print(f"Pares {pares}")
print(f"Impares {impares}")

analisador_numero()