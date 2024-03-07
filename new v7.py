import hashlib
import itertools
import string
import time
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def hash_string(string):
    """Função para criar um hash de uma string usando o algoritmo SHA-256."""
    sha256 = hashlib.sha256()
    sha256.update(string.encode('utf-8'))
    return sha256.hexdigest()

def descriptografar_brute_force(hash_alvo, tamanho_max=4):
    """Função para tentar encontrar uma entrada correspondente a um hash fornecido usando brute force."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    for tamanho in range(1, tamanho_max + 1):
        for tentativa in itertools.product(caracteres, repeat=tamanho):
            palavra = ''.join(tentativa)
            if hash_string(palavra) == hash_alvo:
                return palavra
    return None

def descriptografar_wordlist(hash_alvo, dicionario):
    """Função para tentar encontrar uma entrada correspondente a um hash fornecido usando uma wordlist."""
    for palavra in dicionario:
        if hash_string(palavra) == hash_alvo:
            return palavra
    return None

def carregar_dicionario(nome_arquivo):
    """Função para carregar um dicionário de palavras a partir de um arquivo de texto."""
    with open(nome_arquivo, 'r', encoding='latin-1') as arquivo:
        return [linha.strip() for linha in arquivo]

def cronometrar(funcao, *args):
    """Função para cronometrar o tempo de execução de outra função."""
    inicio = time.time()
    resultado = funcao(*args)
    fim = time.time()
    tempo_execucao = fim - inicio
    return resultado, tempo_execucao

def descriptografar():
    hash_alvo = entry_hash.get().strip()
    if not hash_alvo:
        messagebox.showerror("Erro", "Por favor, insira o hash.")
        return

    if var.get() == 1:
        resultado, tempo_execucao = cronometrar(descriptografar_brute_force, hash_alvo)
        if resultado:
            messagebox.showinfo("Resultado", f"Entrada encontrada: {resultado}\nTempo de execução: {tempo_execucao:.4f} segundos")
        else:
            messagebox.showinfo("Resultado", "Não foi possível encontrar uma entrada correspondente ao hash fornecido.")

    elif var.get() == 2:
        arquivo_dicionario = "rockyou.txt"
        dicionario = carregar_dicionario(arquivo_dicionario)
        resultado, tempo_execucao = cronometrar(descriptografar_wordlist, hash_alvo, dicionario)
        if resultado:
            messagebox.showinfo("Resultado", f"Entrada encontrada: {resultado}\nTempo de execução: {tempo_execucao:.4f} segundos")
        else:
            messagebox.showinfo("Resultado", "Não foi possível encontrar uma entrada correspondente ao hash fornecido.")

    elif var.get() == 3:
        resultado, tempo_execucao_brute = cronometrar(descriptografar_brute_force, hash_alvo)
        resultado_brute = f"Entrada encontrada (brute force): {resultado}\n" if resultado else "Não foi possível encontrar uma entrada correspondente ao hash fornecido utilizando brute force.\n"
        
        arquivo_dicionario = "rockyou.txt"
        dicionario = carregar_dicionario(arquivo_dicionario)
        resultado, tempo_execucao_wordlist = cronometrar(descriptografar_wordlist, hash_alvo, dicionario)
        resultado_wordlist = f"Entrada encontrada (wordlist): {resultado}\n" if resultado else "Não foi possível encontrar uma entrada correspondente ao hash fornecido utilizando wordlist.\n"

def encriptar():
    texto = entry_texto.get().strip()  # Corrigido: entry_hash -> entry_texto
    if not texto:
        messagebox.showerror("Erro", "Por favor, insira o texto para encriptar.")
        return

    hash_encriptado = hash_string(texto)
    messagebox.showinfo("Hash Encriptado", f"O hash encriptado do texto é:\n{hash_encriptado}")

# Inicialização da interface gráfica
root = tk.Tk()
root.title("Hash Crack")

# Adicionando a imagem com o nome da aplicação
image = Image.open("hash_crack_logo.png")
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=photo)
label_image.image = photo
label_image.grid(row=0, column=0, columnspan=3)

# Criação dos widgets
label_texto = ttk.Label(root, text="Texto:")
entry_texto = ttk.Entry(root, width=50)
button_encriptar = ttk.Button(root, text="Encriptar", command=encriptar)
label_hash = ttk.Label(root, text="Hash:")
entry_hash = ttk.Entry(root, width=50)
label_opcao = ttk.Label(root, text="Opção:")
var = tk.IntVar()
radio_brute_force = ttk.Radiobutton(root, text="Brute Force", variable=var, value=1)
radio_wordlist = ttk.Radiobutton(root, text="Wordlist", variable=var, value=2)
radio_ambos = ttk.Radiobutton(root, text="Ambos", variable=var, value=3)
button_descriptografar = ttk.Button(root, text="Descriptografar", command=descriptografar)

# Posicionamento dos widgets
label_texto.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_texto.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
button_encriptar.grid(row=2, column=0, columnspan=3, pady=10)
label_hash.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_hash.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
label_opcao.grid(row=4, column=0, padx=5, pady=5, sticky="w")
radio_brute_force.grid(row=4, column=1, padx=5, pady=5, sticky="w")
radio_wordlist.grid(row=4, column=2, padx=5, pady=5, sticky="w")
button_descriptografar.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
