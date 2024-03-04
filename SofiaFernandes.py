import re
import hashlib
import time
from tqdm import tqdm

def menu(caracteres, wordlist):
    while True:
        escolha = input(""" \033[34m 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
__| |___________________________________________________________________| |__
__   ___________________________________________________________________   __
  | |                                                                   | |  
  | | _   _           _       ____  _   _    _        ____  ____   __   | |  
  | || | | | __ _ ___| |__   / ___|| | | |  / \      |___ \| ___| / /_  | |  
  | || |_| |/ _` / __| '_ \  \___ \| |_| | / _ \ _____ __) |___ \| '_ \ | |  
  | ||  _  | (_| \__ \ | | |  ___) |  _  |/ ___ \_____/ __/ ___) | (_) || |  
  | ||_|_|_|\__,_|___/_| |_| |____/|_| |_/_/   \_\   |_____|____/ \___/ | |  
  | ||  _ \  ___  ___ _ __ _   _ _ __ | |_                              | |  
  | || | | |/ _ \/ __| '__| | | | '_ \| __|                             | |  
  | || |_| |  __/ (__| |  | |_| | |_) | |_                              | |  
  | ||____/ \___|\___|_|   \__, | .__/ \__|                             | |  
  | |                      |___/|_|                                     | |  
__| |___________________________________________________________________| |__
__   ___________________________________________________________________   __
  | |                                                                   | |  
                          
╔════════════════════════════════════════════╗
║ Escolha uma linguagem / Choose a language: ║
╠════════════════════════════════════════════╣                  
║                                            ║
║ 1. Português                               ║
║ 2. English                                 ║
║ 3. Sair / Exit                             ║
╚════════════════════════════════════════════╝

Escolha uma opção / Choose an option: """)
        if escolha == "1":
            return 'portugues'
        elif escolha == "2":
            return 'english'
        elif escolha == "3":
            print("""
╔══════════════════════════════════════════════════╗
║ Menu:                                            ║ 
╠══════════════════════════════════════════════════╣ 
║                                                  ║
║ A fechar o programa... / Leaving the program...  ║
╚══════════════════════════════════════════════════╝
                  """)
            time.sleep(2)
            exit()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def menu_portugues(caracteres, wordlist):
    while True:
        escolha = input("""  
╔════════════════════════════════════╗
║ Menu:                              ║ 
╠════════════════════════════════════╣                  
║                                    ║
║ 1. Desencriptar um hash SHA-256    ║
║ 2. Encriptar uma palavra           ║
║ 3. Sair do programa                ║
╚════════════════════════════════════╝
Escolha uma opção: """)
        if escolha == "1":
            descriptografar_menu(caracteres, wordlist, 'portugues')
        elif escolha == "2":
            criptografar_menu('portugues')
        elif escolha == "3":
            print("""
╔═══════════════════════════════════╗
║ Menu:                             ║ 
╠═══════════════════════════════════╣ 
║                                   ║
║ A fechar o programa...            ║
╚═══════════════════════════════════╝
              """)
            time.sleep(2)
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def menu_english(caracteres, wordlist):
    while True:
        escolha = input("""  
╔═══════════════════════════════════╗
║ Menu:                             ║ 
╠═══════════════════════════════════╣                  
║                                   ║
║ 1. Decrypt SHA-256 hash           ║
║ 2. Encrypt a word                 ║
║ 3. Exit program                   ║
╚═══════════════════════════════════╝
Choose an option: """)
        if escolha == "1":
            descriptografar_menu(caracteres, wordlist, 'english')
        elif escolha == "2":
            criptografar_menu('english')
        elif escolha == "3":
            print("""
╔═══════════════════════════════════╗
║ Menu:                             ║ 
╠═══════════════════════════════════╣ 
║                                   ║
║ Exiting the program...            ║
╚═══════════════════════════════════╝
              """)
            time.sleep(2)
            break
        else:
            print("Invalid option. Please choose a valid option.")

def descriptografar_menu(caracteres, wordlist, linguagem):
    while True:
        if linguagem == 'portugues':
            hash_alvo = input("Escreva a hash SHA-256 para desencriptar (ou 's' para sair): ")
            if hash_alvo.lower() == 's':
                break
        else:
            hash_alvo = input("Write the SHA-256 hash to decrypt (or 'e' to exit): ")
            if hash_alvo.lower() == 'e':
                break
        if not re.match(r'^[a-fA-F0-9]{64}$', hash_alvo):
            if linguagem == 'portugues':
                print("""
╔═══════════════════════════════════════════╗
║ ERRO:                                     ║ 
╠═══════════════════════════════════════════╣ 
║                                           ║
║ Introduza uma hash SHA-256 válida.        ║
╚═══════════════════════════════════════════╝
            """)
            else:
                print("""
╔═══════════════════════════════════════════╗
║ ERROR:                                    ║ 
╠═══════════════════════════════════════════╣ 
║                                           ║
║ Please enter a valid SHA-256 hash.        ║
╚═══════════════════════════════════════════╝
            """)
            continue
        if descriptografar_sha256(hash_alvo, caracteres, 10, wordlist, linguagem):
            if linguagem == 'portugues':
                continuar = input("Pretende desencriptar mais hashes? (s/n): ")
            else:
                continuar = input("Do you want to continue decrypting hashes? (y/n): ")
            if continuar.lower() in ['s', 'y']:
                break

def criptografar_menu(linguagem):
    while True:
        if linguagem == 'portugues':
            palavra = input("Escreva a palavra para encriptar (ou 's' para sair): ")
            if palavra.lower() == 's':
                break
        else:
            palavra = input("Enter the word to encrypt (or 'e' to exit): ")
            if palavra.lower() == 'e':
                break

        hash_cripto = criptografar_sha256(palavra)
        if linguagem == 'portugues':
            print(f"""
            ╔═════════════════╗
            ║    SUCESSO!     ║                                              
            ╚═════════════════╝                  
                  
Palavra encriptada: {hash_cripto}

""")
        else:
            print(f"""
            ╔═════════════════╗
            ║    SUCCESS!     ║                                              
            ╚═════════════════╝

Encrypted word: {hash_cripto}
        
""")
        if linguagem == 'portugues':
            continuar = input("Pretende encriptar mais palavras? (s/n): ")
        else:
            continuar = input("Do you want to continue encrypting words? (y/n): ")
        if continuar.lower() != 's' and continuar.lower() != 'y':
            break

def descriptografar_sha256(hash_alvo, caracteres, comprimento_max, wordlist=None, linguagem='portugues'):
    inicio = time.time()  
    if wordlist is None:
        for comprimento in range(1, comprimento_max + 1):
            for tentativa in tqdm(gerar_combinacoes(caracteres, comprimento), desc=f"Número de caracteres: {comprimento}", leave=False, ascii=True, ncols=100):
                hash_tentativa = hashlib.sha256(tentativa.encode()).hexdigest()
                if hash_tentativa == hash_alvo:
                    fim = time.time()  
                    tempo_decorrido = fim - inicio  
                    if linguagem == 'portugues':
                        print(f"""
            ╔═════════════════╗
            ║    SUCESSO!     ║                                              
            ╚═════════════════╝                                                            
                                                                   
Hash desencriptada: {tentativa};                             
Número de caracteres: {len(tentativa)};                         
Tempo decorrido: {tempo_decorrido:.2f} segundos.              
                    
""")
                    else:
                        print(f"""
            ╔═════════════════╗
            ║    SUCCESS!     ║                                              
            ╚═════════════════╝                                                            
                                                                   
Decrypted hash: {tentativa};                             
Character lenght: {len(tentativa)};                         
Time: {tempo_decorrido:.2f} seconds.              
                    
""")
                    return True
    else:
        for palavra in wordlist:
            palavra = palavra.strip()
            hash_tentativa = hashlib.sha256(palavra.encode()).hexdigest()
            if hash_tentativa == hash_alvo:
                fim = time.time()  
                tempo_decorrido = fim - inicio  
                if linguagem == 'portugues':
                    print(f"""
            ╔═════════════════╗
            ║    SUCESSO!     ║                                              
            ╚═════════════════╝                                                            
                                                                   
Hash desencriptada: {palavra};                             
Número de caracteres: {len(palavra)};                         
Tempo decorrido: {tempo_decorrido:.2f} segundos.              
                    
""")
                else:
                    print(f"""
            ╔═════════════════╗
            ║    SUCCESS!     ║                                              
            ╚═════════════════╝                                                            
                                                                   
Decrypted hash: {palavra};                             
Character lenght: {len(palavra)};                         
Time: {tempo_decorrido:.2f} seconds.              
                    
""")
                return True

    if linguagem == 'portugues':
        print("Não foi possível encontrar uma correspondência para a hash fornecida.")
    else:
        print("No match found for the provided hash.")
    return False

def criptografar_sha256(palavra):
    return hashlib.sha256(palavra.encode()).hexdigest()

def gerar_combinacoes(caracteres, comprimento):
    for palavra in gerar_combinacoes_recursivas(caracteres, "", comprimento):
        yield palavra

def gerar_combinacoes_recursivas(caracteres, prefixo, comprimento):
    if comprimento == 0:
        yield prefixo
    else:
        for caracter in caracteres:
            for palavra in gerar_combinacoes_recursivas(caracteres, prefixo + caracter, comprimento - 1):
                yield palavra

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

wordlist_arquivo = "rockyou.txt"
wordlist = carregar_wordlist(wordlist_arquivo)

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\|!\"#$%&/()=?»«´`+*~^ºª-_.:,;<>@£§€{[]} "

linguagem = menu(caracteres, wordlist)
if linguagem == 'portugues':
    menu_portugues(caracteres, wordlist)
else:
    menu_english(caracteres, wordlist)