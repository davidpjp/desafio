import hashlib
import time

def menu():
    print("===============================================================")
    print("""
       ____  __      _ _                   _       
      / ___|/_/   __| (_) __ _  ___     __| | __ _ 
     | |   / _ \ / _` | |/ _` |/ _ \   / _` |/ _` |
     | |__| (_) | (_| | | (_| | (_) | | (_| | (_| |
      \____\___/ \__,_|_|\__, |\___/   \__,_|\__,_|
            ____         |___/        _            
           | __ )  ___  __ _| |_ _ __(_)____       
           |  _ \ / _ \/ _` | __| '__| |_  /       
           | |_) |  __/ (_| | |_| |  | |/ /        
           |____/ \___|\__,_|\__|_|  |_/___|                       
          """)
    print("================================================================")
    print("Esolha uma opção:")
    print("1 - desincreptar SHA256")
    print("2 - increptar SHA256")

def descriptografar_sha256(hash_alvo, caracteres, comprimento_max):
    for comprimento in range(1, comprimento_max + 1):
        for tentativa in gerar_combinacoes(caracteres, comprimento):
            hash_tentativa = hashlib.sha256(tentativa.encode()).hexdigest()
            if hash_tentativa == hash_alvo:
                return f"Hash descriptografada: {tentativa}"
    return "Hash não pôde ser descriptografada"

def gerar_combinacoes(caracteres, comprimento):
    for palavra in gerar_combinacoes_recursivas(caracteres, "", comprimento):
        yield palavra

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

wordlist_arquivo = "rockyou.txt"
wordlist = carregar_wordlist(wordlist_arquivo)

def descriptografar_sha256_wordlist(hash_alvo, wordlist):
    for tentativa in wordlist:
        hash_tentativa = hashlib.sha256(tentativa.encode()).hexdigest()
        if hash_tentativa == hash_alvo:
            return f"Hash descriptografada: {tentativa}"
    return "Hash não pôde ser descriptografada"

def gerar_combinacoes_recursivas(caracteres, prefixo, comprimento):
    if comprimento == 0:
        yield prefixo
    else:
        for caracter in caracteres:
            for palavra in gerar_combinacoes_recursivas(caracteres, prefixo + caracter, comprimento - 1):
                yield palavra

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:\;<=>?@[]^_`{|}~"
comprimento_maximo = 10

def gerar_hash_sha256(palavra):
    hash_resultado = hashlib.sha256(palavra.encode()).hexdigest()
    return hash_resultado


def main():
    while True:
        menu()

        prompt = input ("Escreva a sua escolha: ")

        if prompt == '1':
            novo_hash = input("Insira uma nova hash SHA256 para tentar desincreptar: ").strip()
            comprimento_hash = len(novo_hash)
            if comprimento_hash != 64:
                print("Feio. Número feio. Põe um número mais bonito.")
                exit()

        if prompt == '2':
            novo_hash = input("Insira uma palavra para transformala numa hash SHA256: ")
            resultado = gerar_hash_sha256(palavra)
            print(f"A hash SHA256 da palavra '{palavra}' é: {resultado}")
        if __name__ == "__main__":
            main()

            # Início do cronômetro
            inicio = time.time()
            
            resultado = descriptografar_sha256_wordlist(novo_hash, wordlist)
            
            # Fim do cronômetro
            fim = time.time()
            
            print(resultado)
            
            # Exibindo o tempo de execução
            print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        else:
            print("Esse não me parece o número favorito da Beatriz, tenta outra vez.")

main()