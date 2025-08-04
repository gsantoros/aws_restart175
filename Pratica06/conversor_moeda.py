import requests
# import datetime

def conversor_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        
        #if "erro" in dados:
        #    return "Moeda invalida,"
        
        return f"""
            Moeda = {moeda} para BRL
            Valor: R$ {float(cotacao['bid']):.2f}
            Máxima: R$ {float(cotacao['high']):.2f}
            Minima: R$ {float(cotacao['low']):.2f}
            Data/Hora: {(cotacao)['create_date']}
            """
            #Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']):.2f} - podem ser incluidos os valores diretos.
    
    except requests.exceptions.RequestException as e:
        return f"Erro ao obter cotação {e}."
    except KeyError:
        return f"Moeda não encontrada ou não suportada."

def main():
    moeda = input(f"Digite o código da moeda para contação (Ex.: USD, EUR, LIB, etc.): ").upper()
    print("\nObtendo cotação...")
    resultado = conversor_moeda(moeda)
    print(resultado)

if __name__ == "__main__":
    main()