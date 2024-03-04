import sys
import hashlib
import itertools
import string
import time

# Function to load a wordlist from a file
def carregar_wordlist(arquivo, encoding='latin'):
    try:
        with open(arquivo, "r", encoding=encoding) as f:
            wordlist = [linha.strip() for linha in f.readlines()]
        return wordlist
    except FileNotFoundError:
        print("Erro: O arquivo", arquivo, "não foi encontrado.")
        return []
    except UnicodeDecodeError:
        print("Erro: Não foi possível decodificar o arquivo", arquivo, "usando o codec", encoding, ".")
        return []

# Function for the main menu
def menu_principal():
    print("""       


.·:''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''':·.
: :  _____ _   _   ___   _____  _____  ____   ______                           _    : :
: : /  ___| | | | / _ \ / __  \|  ___|/ ___|  |  _  \                         | |   : :
: : \ `--.| |_| |/ /_\ \`' / /'|___ \/ /___   | | | |___  ___ _ __ _   _ _ __ | |_  : :
: :  `--. \  _  ||  _  |  / /      \ \ ___ \  | | | / _ \/ __| '__| | | | '_ \| __| : :
: : /\__/ / | | || | | |./ /___/\__/ / \_/ |  | |/ /  __/ (__| |  | |_| | |_) | |_  : :
: : \____/\_| |_/\_| |_/\_____/\____/\_____/  |___/ \___|\___|_|   \__, | .__/ \__| : :
: :                                                                 __/ | |         : :
: :                                                                |___/|_|         : :
'·:.................................................................................:·'
                                                               


                 |---------------------------------------------|
                 | Selecione uma linguagem | Select a language |
                 |---------------------------------------------|
                 | 1.PT                                        |
                 | 2.ENG                                       |
                 | 3.Sair | Exit                               |
                 |---------------------------------------------|
""")

# Function for option 1
def opcao_1():
    print("""                                             
                 |---------------------------------------------|
                 |      Selecionou a linguagem em Português    |
                 |---------------------------------------------|
                 | 1.Desencriptar SHA-256                      |
                 | 2.Encriptar em SHA-256                      |
                 | 3.Exit                                      |
                 |---------------------------------------------|
""")
    
    opcao_1_1 = input("-> Digite o número da opção desejada: ").lower()
    if opcao_1_1 == '1':
        def hash_string(string):
            """Função para criar um hash de uma string usando o algoritmo SHA-256."""
            sha256 = hashlib.sha256()
            sha256.update(string.encode('utf-8'))
            return sha256.hexdigest()
 
        def descriptografar_hash(hash_alvo, caracteres, tamanho_max=4, wordlist=None):
            """Função para tentar encontrar uma entrada correspondente a um hash fornecido."""
            tentativas_feitas = 0
            start_time = time.time()  # Captura o tempo de início
    
            if len(hash_alvo) != 64:  # Check if the hash length is 64 characters
                return None, 0, None
            
            if wordlist is not None:
                for palavra in wordlist:
                    palavra = palavra.strip()
                    tentativas_feitas += 1
                    if hash_string(palavra) == hash_alvo:
                        end_time = time.time()  # Captura o tempo de término
                        tempo_decorrido = end_time - start_time
                        return palavra, tentativas_feitas, round(tempo_decorrido, 1)
            for tamanho in range(1, tamanho_max + 1):
                for tentativa in itertools.product(caracteres, repeat=tamanho):
                    tentativas_feitas += 1
                    palavra = ''.join(tentativa)
                    if hash_string(palavra) == hash_alvo:
                        end_time = time.time()  # Captura o tempo de término
                        tempo_decorrido = end_time - start_time
                        return palavra, tentativas_feitas, round(tempo_decorrido, 1)
            return None, tentativas_feitas, None

        # Input da hash alvo
        hash_alvo = input("Introduza a hash: ")
        print("Aguarde a resolução...")

        # Carregar wordlist, se disponível
        wordlist_arquivo = "rockyou.txt"
        wordlist = carregar_wordlist(wordlist_arquivo)

        # Conjunto de caracteres a serem usados para gerar as tentativas
        caracteres = string.ascii_letters + string.digits + string.punctuation

        # Tentar descriptografar o hash
        entrada_encontrada, tentativas, tempo_decorrido = descriptografar_hash(hash_alvo, caracteres, tamanho_max=6, wordlist=wordlist)  # Ajuste o tamanho máximo conforme necessário

        # Resultados
        if entrada_encontrada:
            print("Entrada encontrada:", entrada_encontrada)
            print("Tentativas feitas:", tentativas)
            print("Tempo decorrido (segundos):", tempo_decorrido)
            time.sleep(4)
            return opcao_1()
        else:
            print("Não foi possível encontrar uma entrada correspondente ao hash fornecido.")
            print("Tentativas feitas:", tentativas)  
            time.sleep(4)
            return opcao_1()      
            
        
    elif opcao_1_1 == '2':
        def hash_sha256(dados):
            sha256 = hashlib.sha256()
            sha256.update(dados.encode('utf-8'))
            return sha256.hexdigest()

        # Solicitar entrada do usuário
        entrada = input("Escreva o texto que ira encriptar em hash SHA-256: ")

        # Medir o tempo de início
        inicio_encriptacao = time.time()

        # Calcular o hash SHA-256 da entrada fornecida
        hash_resultante = hash_sha256(entrada)

        # Medir o tempo de término
        fim_encriptacao = time.time()

        tempo_encriptacao = fim_encriptacao - inicio_encriptacao

        print("Texto encriptado:", hash_resultante)
        print("Tempo de encriptação:", tempo_encriptacao, "segundos")
        time.sleep(4)
        return opcao_1()

        
    elif opcao_1_1 == '3':
        return menu_principal(), main()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(4)
        return opcao_1()
    

# Function for option 2
def opcao_2():
    print("""Select language in English")
                                               
                 |---------------------------------------------|
                 |      Selected the language in English       |
                 |---------------------------------------------|
                 | 1.Decrypt SHA-256                           |
                 | 2.Encrypt in SHA-256                        |
                 | 3.Exit                                      |
                 |---------------------------------------------|
          """)
    opcao_2_1 = input("-> Enter the number of the desired option: ").lower()
    if opcao_2_1 == '1':
        def hash_string(string):
            """Função para criar um hash de uma string usando o algoritmo SHA-256."""
            sha256 = hashlib.sha256()
            sha256.update(string.encode('utf-8'))
            return sha256.hexdigest()
 
        def descriptografar_hash(hash_alvo, caracteres, tamanho_max=4, wordlist=None):
            """Função para tentar encontrar uma entrada correspondente a um hash fornecido."""
            tentativas_feitas = 0
            start_time = time.time()  # Captura o tempo de início
    
            if len(hash_alvo) != 64:  # Check if the hash length is 64 characters
                return None, 0, None
            
            if wordlist is not None:
                for palavra in wordlist:
                    palavra = palavra.strip()
                    tentativas_feitas += 1
                    if hash_string(palavra) == hash_alvo:
                        end_time = time.time()  # Captura o tempo de término
                        tempo_decorrido = end_time - start_time
                        return palavra, tentativas_feitas, round(tempo_decorrido, 1)
            for tamanho in range(1, tamanho_max + 1):
                for tentativa in itertools.product(caracteres, repeat=tamanho):
                    tentativas_feitas += 1
                    palavra = ''.join(tentativa)
                    if hash_string(palavra) == hash_alvo:
                        end_time = time.time()  # Captura o tempo de término
                        tempo_decorrido = end_time - start_time
                        return palavra, tentativas_feitas, round(tempo_decorrido, 1)
            return None, tentativas_feitas, None
        # Carregar uma wordlist, se disponível
        def carregar_wordlist(arquivo, encoding='latin'):
            try:
                with open(arquivo, "r", encoding=encoding) as f:
                    wordlist = [linha.strip() for linha in f.readlines()]
                return wordlist
            except FileNotFoundError:
                print("Erro: O arquivo",arquivo,"não foi encontrado.")
                return []
            except UnicodeDecodeError:
                print("Erro: Não foi possível decodificar o arquivo",arquivo,"usando o codec",encoding,".")
                return []
        # Input da hash alvo
        hash_alvo = input("Enter the hash: ")
        print("Wait for the resolution...")

        # Carregar wordlist, se disponível
        wordlist_arquivo = "rockyou.txt"
        wordlist = carregar_wordlist(wordlist_arquivo)

        # Conjunto de caracteres a serem usados para gerar as tentativas
        caracteres = string.ascii_letters + string.digits + string.punctuation

        # Tentar descriptografar o hash
        entrada_encontrada, tentativas, tempo_decorrido = descriptografar_hash(hash_alvo, caracteres, tamanho_max=6, wordlist=wordlist)  # Ajuste o tamanho máximo conforme necessário

        # Resultados
        if entrada_encontrada:
            print("Entry found:", entrada_encontrada)
            print("Attempts made:", tentativas)
            print("Elapsed time (seconds):", tempo_decorrido)
            time.sleep(4)
            return opcao_2()
        else:
            print("Unable to find an entry matching the given hash")
            print("Attempts made:", tentativas)  
            time.sleep(4)
            return opcao_2()      
            

    elif opcao_2_1 == '2':
        def hash_sha256(dados):
            sha256 = hashlib.sha256()
            sha256.update(dados.encode('utf-8'))
            return sha256.hexdigest()

        # Solicitar entrada do usuário
        entrada = input("Escreva o texto que ira encriptar em hash SHA-256: ")

        # Medir o tempo de início
        inicio_encriptacao = time.time()

        # Calcular o hash SHA-256 da entrada fornecida
        hash_resultante = hash_sha256(entrada)

        # Medir o tempo de término
        fim_encriptacao = time.time()

        tempo_encriptacao = fim_encriptacao - inicio_encriptacao

        print("Encrypted text:", hash_resultante)
        print("Encryption time:", tempo_encriptacao, "segundos")
        time.sleep(4)
        return opcao_2()   
    elif opcao_2_1 == '3':
        return menu_principal(), main()
    else:
        print("Invalid option. Try again.")
        time.sleep(4)
        return opcao_2()

# Function for option 3
def opcao_3():
    print("A sair do programa... | Leaving the program...")
    time.sleep(5)
    sys.exit()

# Main function
def main():
    menu_principal()
    escolha = input("-> Digite o número da opção desejada: ").lower()

    if escolha == '1':
        opcao_1()
    elif escolha == '2':
        opcao_2()
    elif escolha == '3':
        opcao_3()
    else:
        print("Opção inválida. Tente novamente. | Invalid option. Try again.")
        time.sleep(2)
        return menu_principal() ,main()
        
# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
