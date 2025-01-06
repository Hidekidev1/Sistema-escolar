# persistencia.py

import json

def carregar_dados(nome_arquivo):
    """Carrega dados de um arquivo JSON."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []  
    except json.JSONDecodeError:
        print(f"Erro ao carregar os dados de {nome_arquivo}.")
        return []

def salvar_dados(nome_arquivo, dados):
    """Salva dados em um arquivo JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar os dados em {nome_arquivo}: {e}")
