import hashlib
import itertools
import string
import time
import sys
import re  # Import the regular expression module

def hash_string(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def decrypt_hash(target_hash, characters, max_length=4, wordlist=None):
    # Validate SHA-256 hash
    if not re.match(r'^[a-fA-F0-9]{64}$', target_hash):
        print("Error: The provided input does not appear to be a valid SHA-256 hash.")
        return False

    attempts_made = 0
    start_time = time.time()

    if wordlist is not None:
        for word in wordlist:
            word = word.strip()
            attempts_made += 1
            if hash_string(word) == target_hash:
                end_time = time.time()
                elapsed_time = end_time - start_time
                return word, attempts_made, round(elapsed_time, 1)

    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempts_made += 1
            word = ''.join(attempt)
            if hash_string(word) == target_hash:
                end_time = time.time()
                elapsed_time = end_time - start_time
                return word, attempts_made, round(elapsed_time, 1)

    return None, attempts_made, None

def load_wordlist(file, encoding='latin'):
    try:
        with open(file, "r", encoding=encoding) as f:
            wordlist = [line.strip() for line in f.readlines()]
        return wordlist
    except FileNotFoundError:
        print("Error: The file", file, "was not found.")
        return []
    except UnicodeDecodeError:
        print("Error: Unable to decode the file", file, "using the codec", encoding, ".")
        return []

def print_language_menu():
    print("""
  __          __  _                            _______    
 \ \        / / | |                          |__   __|   
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |
  _ _\/_ \/ \___|_|\___\___/|_| |_|_|_|\___|    |_|\___/ 
 / ____| |  | |   /\      |__ \| ____| / /              
| (___ | |__| |  /  \ ______ ) | |__  / /_              
 \___ \|  __  | / /\ \______/ /|___ \| '_ \             
 ____) | |  | |/ ____ \    / /_ ___) | (_) |            
|_____/|_|  |_/_/    \_\  |____|____/ \___/             
|  __ \                           | |                   
| |  | | ___  ___ _ __ _   _ _ __ | |_                  
| |  | |/ _ \/ __| '__| | | | '_ \| __|                 
| |__| |  __/ (__| |  | |_| | |_) | |_                  
|_____/ \___|\___|_|   \__, | .__/ \__|                 
                        __/ | |                         
                       |___/|_|                         """)
    time.sleep(2)

def menu_1():
    print("""
    ///////////////////////////////////////////
    /              SHA-256 MENU               /
    ///////////////////////////////////////////
    /           Select Language:              /
    /                                         /
    /  1. Portuguese (PT)                     /
    /  2. English (EN)                        /
    /  3. Leave                               /
    ///////////////////////////////////////////
    """)
    choice = input("Choose an option: ")
    select_language(choice)

def select_language(option):
    choice = option
    if choice == "1":
        print_menu("pt")
    elif choice == "2":
        print_menu("en")
    elif choice == "3":
        print("\nExiting the program.")
        sys.exit()
    else:
        print("\nInvalid option. Try again.")
        time.sleep(3)
        menu_1()

def print_menu(language):
    if language == "pt":
        print("""
        ///////////////////////////////////////////
        /              MENU SHA-256               /
        ///////////////////////////////////////////
        /  1. Desencriptar hash SHA-256           /
        /  2. Encriptar hash SHA-256 de um texto  /
        /  3. Voltar ao menu de idiomas           /
        /  4. Sair                                /
        ///////////////////////////////////////////
        """)
        menu_pt()
    elif language == "en":
        print("""
        ///////////////////////////////////////////
        /              SHA-256 MENU               /
        ///////////////////////////////////////////
        /  1. Decrypt SHA-256 hash                /
        /  2. Encrypt SHA-256 hash of a text      /
        /  3. Go back to language menu            /
        /  4. Exit                                /
        ///////////////////////////////////////////
        """)
        menu_en()
    else:
        print("Language not supported.")

def menu_pt():
    while True:
        choice = input("Escolha uma opção: ")

        if choice == "1":
            hash_alvo = input("Introduza o hash: ")
            # Validate SHA-256 hash
            if not re.match(r'^[a-fA-F0-9]{64}$', hash_alvo):
                print("Erro: A entrada fornecida não parece ser uma hash SHA256 válida. Tente outra vez com uma hash válida ou escolha outra opção.")
                continue  # Restart the loop
            entrada_encontrada, tentativas, tempo_decorrido = decrypt_hash(hash_alvo, caracteres, max_length=6, wordlist=wordlist)
            if entrada_encontrada:
                print("Entrada encontrada:", entrada_encontrada)
                print("Tentativas feitas:", tentativas)
                print("Tempo decorrido (segundos):", tempo_decorrido)
                time.sleep(3)
                print_menu("pt")
            else:
                print("Não foi possível encontrar uma entrada correspondente ao hash fornecido.")
                time.sleep(3)
                print_menu("pt")
        elif choice == "2":
            texto_para_hash = input("Digite o texto para calcular o hash SHA-256: ")
            resultado_hash = hash_sha256(texto_para_hash)
            print("Hash SHA-256 do texto fornecido:", resultado_hash)
            time.sleep(3)
            print_menu("pt")
        elif choice == "3":
            time.sleep(3)
            menu_1()
        elif choice == "4":
            print("\nSaindo do programa.")
            sys.exit()
        else:
            print("\nOpção inválida. Tente novamente.")
            time.sleep(3)

def menu_en():
    while True:
        choice = input("Choose an Option: ")

        if choice == "1":
            hash_alvo = input("Enter the hash: ")
            # Validate SHA-256 hash
            if not re.match(r'^[a-fA-F0-9]{64}$', hash_alvo):
                print("Error: The provided input does not appear to be a valid SHA-256 hash. Try again choosing another option.")
                continue  # Restart the loop
            entrada_encontrada, tentativas, tempo_decorrido = decrypt_hash(hash_alvo, caracteres, max_length=6, wordlist=wordlist)
            if entrada_encontrada:
                print("Entry Found:", entrada_encontrada)
                print("Attempts made:", tentativas)
                print("Elapsed time (seconds):", tempo_decorrido)
                time.sleep(3)
                print_menu("en")
            else:
                print("Unable to find an entry matching the given hash.")
                time.sleep(3)
                print_menu("en")
        elif choice == "2":
            texto_para_hash = input("Enter text to calculate the hash SHA-256: ")
            resultado_hash = hash_sha256(texto_para_hash)
            print("SHA-256 hash of the provided text:", resultado_hash)
            time.sleep(3)
            print_menu("en")
        elif choice == "3":
            time.sleep(3)
            menu_1()
            
        elif choice == "4":
            print("\nLeaving the program.")
            sys.exit()
        else:
            print("\nInvalid option. Try again.")
            time.sleep(3)

if __name__ == "__main__":
    wordlist_arquivo = "rockyou.txt"
    wordlist = load_wordlist(wordlist_arquivo)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    print_language_menu()
    menu_1()