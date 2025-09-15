import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Função para abrir a imagem
def abrir_imagem():
    caminho_arquivo = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=[("Imagem", "*.jpg;*.jpeg;*.png;*.bmp")])
    
    if caminho_arquivo:
        # Abrir a imagem escolhida
        imagem = Image.open(caminho_arquivo)
        
        # Converter para o formato que o Tkinter entende
        imagem_tk = ImageTk.PhotoImage(imagem)
        
        # Atualizar a imagem no Canvas
        canvas.create_image(0, 0, image=imagem_tk, anchor="nw")
        
        # Armazenar a imagem para futuros ajustes
        global imagem_original
        imagem_original = imagem
        global caminho_imagem
        caminho_imagem = caminho_arquivo

        # Atualizar a imagem no Canvas
        canvas.image = imagem_tk

# Função para centralizar a imagem
def centralizar_imagem():
    if imagem_original:
        imagem_tk = ImageTk.PhotoImage(imagem_original)
        canvas.create_image(400, 300, image=imagem_tk, anchor="center")
        canvas.image = imagem_tk

# Função para redimensionar a imagem para preencher o formulário
def estender_imagem():
    if imagem_original:
        # Redimensionar a imagem para 800x600
        imagem_redimensionada = imagem_original.resize((800, 600))
        imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
        
        # Atualizar a imagem no Canvas
        canvas.create_image(0, 0, image=imagem_tk, anchor="nw")
        canvas.image = imagem_tk

# Função para escolher o diretório onde a imagem será salva
def escolher_pasta():
    caminho_pasta = filedialog.askdirectory(title="Escolha a pasta para salvar a imagem")
    if caminho_pasta:
        label_resultado.config(text=f"Pasta escolhida: {caminho_pasta}", fg="green")
        global caminho_pasta_salvar
        caminho_pasta_salvar = caminho_pasta

# Função para salvar a imagem no diretório escolhido
def salvar_imagem():
    if imagem_original and caminho_pasta_salvar:
        # Salvar a imagem na pasta escolhida
        nome_arquivo = os.path.basename(caminho_imagem)
        caminho_destino = os.path.join(caminho_pasta_salvar, nome_arquivo)
        
        # Salvar a imagem
        imagem_original.save(caminho_destino)
        label_resultado.config(text=f"Imagem salva em: {caminho_destino}", fg="green")

# Função para limpar os campos
def limpar_campos():
    canvas.delete("all")
    label_resultado.config(text="")
    global imagem_original, caminho_imagem, caminho_pasta_salvar
    imagem_original = None
    caminho_imagem = None
    caminho_pasta_salvar = None

# Função para sair
def sair():
    janela.quit()

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Imagens")
janela.geometry("800x600")  # Definir o tamanho da janela
janela.config(bg="#f2f2f2")  # Cor de fundo da janela

# Título
titulo = tk.Label(janela, text="Escolha, Ajuste e Salve sua Imagem", font=("Helvetica", 14, "bold"), bg="#f2f2f2")
titulo.grid(row=0, column=0, columnspan=3, pady=10)

# Frame para o Canvas e a barra de rolagem
frame_canvas = tk.Frame(janela)
frame_canvas.grid(row=1, column=0, columnspan=3, pady=5)

# Adicionar a barra de rolagem horizontal e vertical
scrollbar_vertical = tk.Scrollbar(frame_canvas, orient="vertical")
scrollbar_vertical.pack(side="right", fill="y")

scrollbar_horizontal = tk.Scrollbar(frame_canvas, orient="horizontal")
scrollbar_horizontal.pack(side="bottom", fill="x")

# Criar o Canvas com as barras de rolagem
canvas = tk.Canvas(frame_canvas, yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set, width=800, height=500)
canvas.pack()

# Configurar as barras de rolagem
scrollbar_vertical.config(command=canvas.yview)
scrollbar_horizontal.config(command=canvas.xview)

# Frame para os botões (usando grid para organizar em colunas)
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=2, column=0, columnspan=3, pady=10)

# Botão para abrir a imagem
botao_abrir = tk.Button(frame_botoes, text="Abrir Imagem", command=abrir_imagem, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), width=20)
botao_abrir.grid(row=0, column=0, padx=5, pady=5)

# Botão para centralizar a imagem
botao_centralizar = tk.Button(frame_botoes, text="Centralizar Imagem", command=centralizar_imagem, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"), width=20)
botao_centralizar.grid(row=0, column=1, padx=5, pady=5)

# Botão para redimensionar a imagem
botao_estender = tk.Button(frame_botoes, text="Estender Imagem", command=estender_imagem, bg="#FF9800", fg="white", font=("Helvetica", 10, "bold"), width=20)
botao_estender.grid(row=0, column=2, padx=5, pady=5)

# Botões para salvar e escolher pasta
botao_escolher_pasta = tk.Button(frame_botoes, text="Escolher Pasta", command=escolher_pasta, bg="#009688", fg="white", font=("Helvetica", 10, "bold"), width=20)
botao_escolher_pasta.grid(row=1, column=0, padx=5, pady=5)

botao_salvar = tk.Button(frame_botoes, text="Salvar Imagem", command=salvar_imagem, bg="#FF5722", fg="white", font=("Helvetica", 10, "bold"), width=20)
botao_salvar.grid(row=1, column=1, padx=5, pady=5)

# Botão para limpar os campos
botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_campos, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"), width=20)
botao_limpar.grid(row=1, column=2, padx=5, pady=5)

# Botão para sair
botao_sair = tk.Button(frame_botoes, text="Sair", command=sair, bg="#9E9E9E", fg="white", font=("Helvetica", 10, "bold"), width=20)
botao_sair.grid(row=2, column=0, columnspan=3, pady=5)

# Label para mostrar o resultado da operação
label_resultado = tk.Label(janela, text="", font=("Helvetica", 10), bg="#f2f2f2")
label_resultado.grid(row=3, column=0, columnspan=3, pady=10)

# Variáveis globais
imagem_original = None
caminho_imagem = None
caminho_pasta_salvar = None

# Rodar a aplicação
janela.mainloop()