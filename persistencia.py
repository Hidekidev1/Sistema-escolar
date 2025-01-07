import json

def carregar_dados(arquivo):
    """Carrega os dados de um arquivo JSON e retorna o conteúdo."""
    try:
        with open(arquivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado. Criando novo arquivo.")
        return []  # Retorna uma lista vazia se o arquivo não for encontrado
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {arquivo}.")
        return []

def salvar_dados(nome_arquivo, dados):
    """Salva dados em um arquivo JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar os dados em {nome_arquivo}: {e}")
