import sqlite3
import tkinter as tk
from tkinter import messagebox

def gravar_aluno():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    celular = entry_celular.get()
    email = entry_email.get()

    if not nome or not endereco or not cidade or not estado or not celular or not email:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    # Usando uma cidade e estado fictícios simplificados para demonstração:
    # No real, teria fk para cidade_id, estado_id conforme modelo anterior.
    cursor.execute('''
    INSERT INTO alunos (nome, endereco, cidade_id, celular, email)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, endereco, 1, celular, email))  # cidade_id fixo para simplificar
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
    limpar_campos()

def mostrar_alunos():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ra, nome FROM alunos')
    alunos = cursor.fetchall()
    conn.close()

    text_memo.delete('1.0', tk.END)
    for aluno in alunos:
        text_memo.insert(tk.END, f"RA: {aluno[0]} - Nome: {aluno[1]}\n")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("Cadastro de Alunos")

# Campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, sticky='e')
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Endereço:").grid(row=1, column=0, sticky='e')
entry_endereco = tk.Entry(root, width=40)
entry_endereco.grid(row=1, column=1)

tk.Label(root, text="Cidade:").grid(row=2, column=0, sticky='e')
entry_cidade = tk.Entry(root, width=40)
entry_cidade.grid(row=2, column=1)

tk.Label(root, text="Estado:").grid(row=3, column=0, sticky='e')
entry_estado = tk.Entry(root, width=40)
entry_estado.grid(row=3, column=1)

tk.Label(root, text="Celular:").grid(row=4, column=0, sticky='e')
entry_celular = tk.Entry(root, width=40)
entry_celular.grid(row=4, column=1)

tk.Label(root, text="Email:").grid(row=5, column=0, sticky='e')
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=5, column=1)

# Botões
btn_gravar = tk.Button(root, text="Gravar Aluno", command=gravar_aluno)
btn_gravar.grid(row=6, column=0, pady=10)

btn_mostrar = tk.Button(root, text="Mostrar Todos", command=mostrar_alunos)
btn_mostrar.grid(row=6, column=1, pady=10)

# Memo para exibir os alunos
text_memo = tk.Text(root, height=10, width=60)
text_memo.grid(row=7, column=0, columnspan=2)

root.mainloop()