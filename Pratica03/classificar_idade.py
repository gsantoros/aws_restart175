"""
2- Classificador de Idade
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:
Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos)
Idoso (60 anos ou mais).
"""

idade_indicada = int(input("Insira a sua idade: "))

if idade_indicada <= 12:
    print(f"Como você tem {idade_indicada} anos, você é uma criança.")
elif idade_indicada <= 17:
    print(f"Como você tem {idade_indicada} anos, você é adolescente.")
elif idade_indicada <= 59:
    print(f"Como você tem {idade_indicada} anos, você é adulto(a).")
else:
    print(f"Como você tem {idade_indicada} anos, você é idoso(a).")