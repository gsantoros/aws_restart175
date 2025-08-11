"""
3. Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if  "erro" in dados:
            return "CEP não encontrado."
        return f"""
        CEP:  {dados['cep']}
        Logradouro: {dados['logradouro']}
        Bairro: {dados['bairro']}
        Cidade: {dados['localidade']}
        Estado: {dados['uf']}
        """
    except requests.exceptions.RequestException as e:
        print (f"Ocorreu um erro na consulta do CEP: {e}")

def main():
    cep = input("Digite um CEP para ser consultado (apenas números): ")
    if len(cep) == 8 and cep.isdigit():
        print("\nConsultando CEP...")
        resultado = consultar_cep(cep)
        print(resultado)
    else:
        print("CEP inválido. Certigique-se que o CEP tem apenas 8 números.")

if __name__ == "__main__":
    main()