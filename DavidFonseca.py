import hashlib
import webbrowser

def menu():
    print("------>MENU<------")
    print("")
    print("1 - SHA256")
    print("2 - OTHER")
    print("3 - Sair")

def open_link(url):
    webbrowser.open_new(url)

def souls_like():
    escolha = input("Gostas de SoulsLike?('Sim' ou 'Não'): ")
    if escolha == "Sim":
        print("Boa escolha Tarnished!")
    elif escolha == "Não":
        print("Tens que gostar, é incrível!")
    else:
        open_link("https://www.instant-gaming.com/en/4824-buy-steam-elden-ring-pc-game-steam-europe/")        

def descriptografar_sha256(hash_alvo, caracteres, comprimento_max, wordlist=None):
    if len(hash_alvo) != 64:
        return "Erro! A hash SHA256 deve ter exatamente 64 caracteres."
    else:            
        if wordlist is None:
            for comprimento in range(1, comprimento_max + 1):
                for tentativa in gerar_combinacoes(caracteres, comprimento):
                    hash_tentativa = hashlib.sha256(tentativa.encode()).hexdigest()
                    if hash_tentativa == hash_alvo:
                        return f"Hash descriptografada: {tentativa}"
        else:
            for palavra in wordlist:
                palavra = palavra.strip()
                hash_tentativa = hashlib.sha256(palavra.encode()).hexdigest()
                if hash_tentativa == hash_alvo:
                    return f"Hash descriptografada: {palavra}"
            return " "

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

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:\;<=>?@[]^_`{|}~"
comprimento_maximo = 10

def main():
    while True:
        menu()

        prompt = input("Esolha um método de desincriptação: ")
        
        if prompt == '1':
            novo_hash = input("Insira uma nova hash SHA256 para tentar descifrar: ")  
            resultado2 = descriptografar_sha256(novo_hash, None, None, wordlist)
            print(resultado2)
            if resultado2 not in wordlist:
                resultado1 = descriptografar_sha256(novo_hash, caracteres, comprimento_maximo, None)
                print(resultado1)
        elif prompt == "2":
            souls_like()
        elif prompt == "3":
            print("Obrigado por usar.")
            exit()
        else:
            print("Erro, insira uma opção válida")    

main()