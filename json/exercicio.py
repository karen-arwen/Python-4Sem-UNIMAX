import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
import os

ARQUIVO_DADOS = 'cliente.json'

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Pessoas")
        self.root.geometry("450x500")
        self.root.resizable(False, False)

        # Variáveis tkinter para campos
        self.nome_var = tk.StringVar()
        self.endereco_var = tk.StringVar()
        self.cidade_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.foto_path = None
        self.foto_imgtk = None

        # Frame para os campos
        form_frame = tk.Frame(root, padx=15, pady=10)
        form_frame.pack(fill="both", expand=True)

        tk.Label(form_frame, text="Nome:", anchor="w").grid(row=0, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.nome_var, width=40).grid(row=0, column=1, pady=5, sticky="w")

        tk.Label(form_frame, text="Endereço:", anchor="w").grid(row=1, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.endereco_var, width=40).grid(row=1, column=1, pady=5, sticky="w")

        tk.Label(form_frame, text="Cidade:", anchor="w").grid(row=2, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.cidade_var, width=40).grid(row=2, column=1, pady=5, sticky="w")

        tk.Label(form_frame, text="Estado:", anchor="w").grid(row=3, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.estado_var, width=40).grid(row=3, column=1, pady=5, sticky="w")

        # Espaço para foto (removi width e height para ajustar natural)
        self.foto_label = tk.Label(form_frame, text="Imagem (duplo clique para carregar)",
                                   bg="lightgray", relief="ridge")
        self.foto_label.grid(row=4, column=0, columnspan=2, pady=15, sticky="nsew")
        self.foto_label.bind("<Double-Button-1>", self.carregar_foto)

        # Configurar o grid para expandir a linha da foto e coluna do formulário
        form_frame.grid_rowconfigure(4, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        # Frame rodapé para botões coloridos
        rodape_frame = tk.Frame(root, bd=1, relief="raised", padx=10, pady=10)
        rodape_frame.pack(side="bottom", fill="x")

        # Botões coloridos com cores
        tk.Button(rodape_frame, text="Gravar", width=10, bg="#4CAF50", fg="white", command=self.gravar).pack(side="left", padx=10)
        tk.Button(rodape_frame, text="Pesquisar", width=10, bg="#2196F3", fg="white", command=self.pesquisar).pack(side="left", padx=10)
        tk.Button(rodape_frame, text="Limpar", width=10, bg="#FF9800", fg="black", command=self.limpar).pack(side="left", padx=10)
        tk.Button(rodape_frame, text="Sair", width=10, bg="#f44336", fg="white", command=root.quit).pack(side="right", padx=10)

        # Atualizar a interface para garantir tamanho do label
        root.update()

    def carregar_foto(self, event):
        caminho = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Arquivos de imagem", "*.png;*.jpg;*.jpeg;*.gif"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            self.foto_path = caminho
            self.mostrar_imagem(caminho)

    def mostrar_imagem(self, caminho):
        img = Image.open(caminho)
        label_width = self.foto_label.winfo_width()
        label_height = self.foto_label.winfo_height()

        if label_width < 10 or label_height < 10:
            # Tamanho padrão se label ainda não renderizado
            label_width, label_height = 400, 200

        img.thumbnail((label_width, label_height))
        self.foto_imgtk = ImageTk.PhotoImage(img)
        self.foto_label.config(image=self.foto_imgtk, text='')

    def gravar(self):
        nome = self.nome_var.get().strip()
        if not nome:
            messagebox.showwarning("Erro", "Nome é obrigatório para cadastro.")
            return

        cadastro = self.carregar_dados()
        dados_pessoa = {
            "nome": nome,
            "endereco": self.endereco_var.get().strip(),
            "cidade": self.cidade_var.get().strip(),
            "estado": self.estado_var.get().strip(),
            "foto": self.foto_path or ""
        }
        cadastro = [p for p in cadastro if p['nome'].lower() != nome.lower()]
        cadastro.append(dados_pessoa)

        with open(ARQUIVO_DADOS, 'w') as arquivo:
            json.dump(cadastro, arquivo, indent=4)
        messagebox.showinfo("Sucesso", "Cadastro gravado com sucesso.")
        self.limpar(campos=True)

    def pesquisar(self):
        nome = self.nome_var.get().strip()
        if not nome:
            messagebox.showwarning("Erro", "Digite o nome para pesquisar.")
            return

        cadastro = self.carregar_dados()
        pessoa = next((p for p in cadastro if p['nome'].lower() == nome.lower()), None)

        if pessoa:
            self.endereco_var.set(pessoa.get('endereco', ''))
            self.cidade_var.set(pessoa.get('cidade', ''))
            self.estado_var.set(pessoa.get('estado', ''))
            foto = pessoa.get('foto', '')
            if foto and os.path.exists(foto):
                self.foto_path = foto
                self.mostrar_imagem(foto)
            else:
                self.foto_path = None
                self.foto_label.config(image='', text="Imagem (duplo clique para carregar)")
            messagebox.showinfo("Encontrado", f"Dados da pessoa {nome} carregados.")
        else:
            messagebox.showinfo("Não encontrado", "Pessoa não encontrada.")
            self.limpar(campos=False)

    def limpar(self, campos=True):
        if campos:
            self.nome_var.set('')
            self.endereco_var.set('')
            self.cidade_var.set('')
            self.estado_var.set('')
            self.foto_path = None
            self.foto_imgtk = None
            self.foto_label.config(image='', text="Imagem (duplo clique para carregar)")

    def carregar_dados(self):
        if not os.path.exists(ARQUIVO_DADOS):
            return []
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            return json.load(arquivo)

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()