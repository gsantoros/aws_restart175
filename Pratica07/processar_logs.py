"""
1. Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning.
Calcule a média e o desvio padrão do tempo de exercução constantes.
"""

import pandas as pd

def processa_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media_tempo:.2f} segundos.")
        print(f"Desvio Padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception:
        print("Erro ao processar o arquivo.")

nome_arquivo = input("Digite o node do arquivo de log: ")
processa_logs_treinamento(nome_arquivo)