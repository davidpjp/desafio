import hashlib
import itertools

def criar_hash_senha(senha):
    sha256 = hashlib.sha256()
    sha256.update(senha.encode('utf-8'))
    return sha256.hexdigest()

# Função para carregar uma wordlist de um arquivo
def carregar_wordlist(caminho_arquivo, encoding='utf-8'):
    with open(caminho_arquivo, 'r', encoding=encoding, errors='ignore') as file:
        return [linha.strip() for linha in file.readlines()]

# Função para desencriptar usando wordlist
def desencriptar_wordlist(hash_usuario, wordlist):
    senha_encontrada = None

    for senha in wordlist:
        if criar_hash_senha(senha) == hash_usuario:
            senha_encontrada = senha
            
            break  # Parar a busca se a senha for encontrada na wordlist

    return senha_encontrada

# Função para desencriptar usando brute force
def desencriptar_brute_force(hash_usuario):
    caracteres_possiveis = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;:,.<>?'
    
    for tamanho_senha in range(1, len(hash_usuario) + 1):
        for tentativa in itertools.product(caracteres_possiveis, repeat=tamanho_senha):
            senha = ''.join(tentativa)
            hash_tentativa = criar_hash_senha(senha)

            if hash_tentativa == hash_usuario:
                return senha

    return None

# Entrada da hash do usuário

# Verificar se a hash fornecida tem o comprimento correto

# Carregar a wordlist de senhas
wordlist = carregar_wordlist('rockyou.txt')  # Substitua pelo caminho correto do seu arquivo

# Menu
senha_correspondente = None
while True:
    print(""" 
    _____                                                                                                                _____ 
   ( ___ )                                                                                                              ( ___ )
    |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
    |   |                                                                                                                |   | 
    |   |                                                                                                                |   | 
    |   |    ██╗ ██╗ ███████╗██████╗    ██████╗ ██████╗ ███████╗███████╗██╗██████╗ ███████╗███╗   ██╗████████╗███████╗   |   | 
    |   |   ████████╗██╔════╝██╔══██╗   ██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝   |   | 
    |   |   ╚██╔═██╔╝███████╗██████╔╝   ██████╔╝██████╔╝█████╗  ███████╗██║██║  ██║█████╗  ██╔██╗ ██║   ██║   █████╗     |   | 
    |   |   ████████╗╚════██║██╔══██╗   ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝     |   | 
    |   |   ╚██╔═██╔╝███████║██║  ██║██╗██║     ██║  ██║███████╗███████║██║██████╔╝███████╗██║ ╚████║   ██║   ███████╗   |   | 
    |   |    ╚═╝ ╚═╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝   |   | 
    |   |                                                                                                                |   | 
    |   |                                                                                                                |   | 
    |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
   (_____)                                                                                                              (_____)
          
          
    1. Desencriptar hash (SHA-256)
    2. Sair 
          
          """)

    escolha = input("Escolha uma opção (1/2): ")

    if escolha == '1':
        hash_usuario = input("Escreva a hash para desencriptar: ")
        if len(hash_usuario) != 64 or not all(c in '0123456789abcdefABCDEF' for c in hash_usuario):
            print("Hash inválida. Certifique-se de que a hash é uma SHA-256 válida.")
            exit()
        senha_correspondente = desencriptar_wordlist(hash_usuario, wordlist)
        if senha_correspondente is None:
            senha_correspondente = desencriptar_brute_force(hash_usuario)
        break
    elif escolha == '2':
        print("A sair do programa.")
        exit()
    else:
        print("Opção inválida. Escolha novamente.")
        
# Exibir resultado
if senha_correspondente:
    print(f"A senha correspondente à hash é: {senha_correspondente}")
else:
    print("Senha não encontrada.")
