import csv

def ler_dados_csv(nome_arquivo):
    """
    Lê um arquivo CSV e retorna uma lista de dicionários, onde cada dicionário
    representa uma linha com os cabeçalhos como chaves.
    
    Args:
        nome_arquivo (str): Caminho do arquivo CSV
        
    Returns:
        list: Lista de dicionários contendo os dados do CSV
        
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado
        csv.Error: Se houver erro na leitura do CSV
    """
    dados = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                dados.append(dict(linha))
        return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []
    except csv.Error:
        print(f"Erro: Falha ao ler o arquivo CSV '{nome_arquivo}'.")
        return []