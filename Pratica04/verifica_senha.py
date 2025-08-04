"""
3. Crie um programa que verifique se uma senha é forte.
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.
O programa deve continuar pedindo senhas até que uma
válida seja inserida ou o usuário digite 'sair'.
"""

while True:
    senha = input("Digite a senha ou 'sair' para encerrar: ")

    # O programa verifica se o usuário pretende sair.
    if senha.lower() == "sair":
        break

    # O program verifica se há o comprimento minimo na senha.
    if len(senha) < 8:
        print("Senha fraca. A senha precisa conter pelos menos 8 caracteres.")
        continue
    
    if not any(caracter.isdigit() for caracter in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    if not any(caracter.isalpha() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra.")
        continue

    if not any(caracter.isdigit() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra maiúscula.")
        continue

    # Chegando até aqui, a senha é válida.
    print("Parabéns, a senha é forte e válida.")
    break