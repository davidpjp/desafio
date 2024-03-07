import hashlib

def hash_string(string):
    """Função para criar um hash de uma string usando o algoritmo SHA-256."""
    sha256 = hashlib.sha256()
    sha256.update(string.encode('utf-8'))
    return sha256.hexdigest()

def descriptografar_hash(hash_alvo, dicionario):
    """Função para tentar encontrar uma entrada correspondente a um hash fornecido."""
    for palavra in dicionario:
        if hash_string(palavra) == hash_alvo:
            return palavra
    return None

# Dicionário de palavras
dicionario = ["hello", "world", "python", "openai", "chatgpt", "gpt3", "abc"]

# Hash alvo para descriptografar
hash_alvo = "rockyou.txt"

# Tentar descriptografar o hash
entrada_encontrada = descriptografar_hash(hash_alvo, dicionario)

if entrada_encontrada:
    print("Entrada encontrada:", entrada_encontrada)
else:
    print("Não foi possível encontrar uma entrada correspondente ao hash fornecido.")
