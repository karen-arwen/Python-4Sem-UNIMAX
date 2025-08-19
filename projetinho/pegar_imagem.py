import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Pillow (PIL) para manipulação de imagens

# Função para abrir a janela de arquivos e escolher a imagem
def abrir_imagem():
    # Abrir a janela de diálogo para selecionar um arquivo
    caminho_arquivo = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=[("Imagem", "*.jpg;*.jpeg;*.png;*.bmp")])
    
    if caminho_arquivo:
        # Abrir a imagem usando Pillow
        imagem = Image.open(caminho_arquivo)
        
        # Converter a imagem para um formato compatível com o Tkinter (ImageTk)
        imagem_tk = ImageTk.PhotoImage(imagem)
        
        # Atualizar o widget de imagem com a imagem escolhida
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk  # Isso é necessário para manter a referência da imagem
        label_imagem.pack()

# Criar a janela principal
janela = tk.Tk()
janela.title("Abrir e Exibir Imagem")
janela.geometry("500x500")  # Tamanho da janela

# Adicionar um botão para abrir a imagem
botao_abrir = tk.Button(janela, text="Abrir Imagem", command=abrir_imagem)
botao_abrir.pack(pady=20)

# Criar um label onde a imagem será exibida
label_imagem = tk.Label(janela)
label_imagem.pack(pady=10)

# Rodar a aplicação
janela.mainloop()