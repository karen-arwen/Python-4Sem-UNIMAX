import tkinter as tk
import re

# Função de validação
def validar_entrada():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    
    # Validar nome: não pode ser vazio ou ter apenas espaços
    if not nome.strip():
        label_resultado.config(text="Nome não pode ser vazio!", fg="red")
    
    # Validar idade: deve ser um número positivo
    elif not idade.isdigit() or int(idade) <= 0:
        label_resultado.config(text="Idade deve ser um número positivo!", fg="red")
    
    # Validar e-mail com regex
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        label_resultado.config(text="E-mail inválido!", fg="red")
    
    else:
        label_resultado.config(text=f"Cadastro realizado! Nome: {nome}, Idade: {idade}, E-mail: {email}", fg="green")

# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário de Cadastro")

# Labels
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

# Entry para o nome
entry_nome = tk.Entry(janela)
entry_nome.pack()

# Labels
label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()

# Entry para a idade
entry_idade = tk.Entry(janela)
entry_idade.pack()

# Labels
label_email = tk.Label(janela, text="E-mail:")
label_email.pack()

# Entry para o e-mail
entry_email = tk.Entry(janela)
entry_email.pack()

# Botão de validar
botao_validar = tk.Button(janela, text="Validar", command=validar_entrada)
botao_validar.pack()

# Label para mostrar mensagens de erro ou sucesso
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Rodar a aplicação
janela.mainloop()
