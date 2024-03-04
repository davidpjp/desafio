import os
import tkinter as tk
from tkinter import ttk, messagebox
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import hashlib
import itertools
import string

class DecryptHashApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Descriptografar Hash")

        # Configurar o estilo para widgets ttk
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", background="#ccc")
        style.configure("TLabel", font=("Helvetica", 18))
        style.configure("TEntry", font=("Helvetica", 18))

        # Configurar o notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=30)

        # Página principal
        self.main_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.main_frame, text="Principal")

        # Widgets na página principal
        label_hash = ttk.Label(self.main_frame, text="Introduz hash:", style="TLabel")
        label_hash.pack(pady=15)

        self.entry_hash = ttk.Entry(self.main_frame, font=("Helvetica", 18))
        self.entry_hash.pack(pady=15)

        # Botão Descriptografar
        button_decrypt = ttk.Button(self.main_frame, text="Descriptografar", command=self.realizar_descriptografia, style="TButton")
        button_decrypt.pack(pady=30)

        # Página de resultados
        self.result_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.result_frame, text="Resultados")

        # Adiciona os widgets à aba "Resultados"
        self.result_text = tk.Text(self.result_frame, height=15, width=60, state=tk.DISABLED, font=("Helvetica", 18))
        self.result_text.pack(padx=30, pady=30)

        # Configuração da aba "Resultados"
        self.result_tab = 2

        # Menus
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Sair", command=self.on_exit)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Copiar", command=self.on_copy)
        edit_menu.add_command(label="Colar", command=self.on_paste)

        # Wordlist
        self.wordlist = self.carregar_wordlist("C:\\Users\\abalouta\\Downloads\\rockyou.txt")  # Substitua pelo caminho real do seu arquivo

    def on_exit(self):
        self.root.destroy()

    def on_copy(self):
        messagebox.showinfo("Copiar", "Copiado!")

    def on_paste(self):
        messagebox.showinfo("Colar", "Colado!")

    def realizar_descriptografia(self):
        hash_alvo = self.entry_hash.get()

        if len(hash_alvo) != 64:
            messagebox.showwarning("Comprimento Inválido", "São apenas permitidas hashes SHA-256 válidas.")
            return

        if not hash_alvo:
            messagebox.showwarning("Campo Vazio", "Por favor, insira um hash para descriptografar.")
            return

        # Agendar a execução da descriptografia na thread principal
        self.root.after(0, lambda: self.executar_realizar_descriptografia(hash_alvo))

    def executar_realizar_descriptografia(self, hash_alvo):
        entrada_encontrada = self.descriptografar_hash(hash_alvo, tamanho_max=6)

        if entrada_encontrada:
            # Adiciona o resultado à aba "Resultados"
            self.notebook.select(self.result_tab)
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Resultado da Descriptografia: " + entrada_encontrada)
            self.result_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Não Encontrado", "Não foi possível encontrar uma entrada correspondente ao hash fornecido.")

    def descriptografar_hash(self, hash_alvo, tamanho_max=4):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        total_combinacoes = sum(len(caracteres) ** tamanho for tamanho in range(1, tamanho_max + 1))

        with ProcessPoolExecutor() as executor:
            # Tentar descriptografar com cada palavra da wordlist
            for palavra in tqdm(self.wordlist, desc="Descriptografando com Wordlist", unit="palavras"):
                if self.hash_string(palavra) == hash_alvo:
                    return palavra

            # Se não encontrou com a wordlist, tentar combinações normais
            chunk_size = 10000  # Ajuste o tamanho do bloco conforme necessário
            chunks = ["".join(tentativa) for tentativa in itertools.product(caracteres, repeat=tamanho_max)]
            chunks = [chunks[i:i + chunk_size] for i in range(0, len(chunks), chunk_size)]

            for chunk in tqdm(executor.map(self.hash_string, chunks), total=total_combinacoes, desc="Descriptografando", unit="combinacoes"):
                for palavra in chunk:
                    if palavra == hash_alvo:
                        return palavra

        return None

    def hash_string(self, s):
        sha256 = hashlib.sha256()
        sha256.update(s.encode('latin'))
        return sha256.hexdigest()

    def carregar_wordlist(self, caminho):
        try:
            with open(caminho, "r", encoding="latin") as arquivo:
                return [linha.strip() for linha in arquivo.readlines()]
        except FileNotFoundError:
            messagebox.showerror("Erro", "O arquivo da wordlist não foi encontrado. Verifique o caminho.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DecryptHashApp(root)
    root.mainloop()
