"""
2. 
Crie um programa que permita a um professor registrar as notas de uma turma.
O programa deve continuar solicitando notas até que o professor digite 'fim'.
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando.
No final, deve exibir a média da turma.
"""

lista_notas = []

while True: #Essa linha vai manter o programa aberto até que seja digitado 'fim'
    
    try:
        entrada = input("Digite uma nota do aluno (ou 'fim' para encerrar): ")
        if entrada == "fim":
            break

        nota = float(entrada)
        if 0 <= nota <= 10:
            lista_notas.append(nota)
        else:
            print("Nota inválida, digite um valor entre 0 e 10.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim' para encerrar.")

if lista_notas:
    media = sum(lista_notas) / len(lista_notas)
    print(f"Média da turma: {media:.2f}")
    print(f"Total de notas válidas registradas: {len(lista_notas)}.")
else:
    print("Nenhuma nota foi lançada.")