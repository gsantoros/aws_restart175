"""
2. Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual
de trás para frente, ignorando espaços e pontuação). Se o resultado é True,
responda “Sim”, se o resultado for False, responda “Não”.
"""

def is_palindromo(texto):
    texto_limpo = ''.join(char.lower()
                        for char in texto
                        if char.isalnum())
    
    return texto_limpo == texto_limpo[::-1]

frase  = input("Informe uma expressão ou frase para ser verificada: ")
resultado = is_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"A frase '{frase}' é palíndromo? {resposta}.")