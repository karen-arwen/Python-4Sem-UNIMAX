import tkinter as tk

nome_produto = tk.StringVar()
quantidade = tk.IntVar()
preco_unitario = tk.DoubleVar()

# Criar a janela principal
form = tk.Tk()
form.geometry("300x200")
form.title("Calculadora de Compras")

label_nome = tk.Label(form, text="Nome do Produto: ")
label_nome.grid(row=0, column=0, padx=10, pady=5)
nom_prod = tk.Entry(form)
nom_prod.grid(row=0, column=1, padx=10, pady=5)
nom_prod = tk.Entry(form, textvariable=nome_produto)

label_quantidade = tk.Label(form, text="Quantidade: ")
label_quantidade.grid(row=1, column=0, padx=10, pady=5)
num_qnt = tk.Entry(form)
num_qnt.grid(row=1, column=1, padx=10, pady=5)
num_qnt = tk.Entry(form, textvariable=preco_unitario)


label_total = tk.Label(form, text="Total: R$")
label_total.grid(row=3, column=0, padx=10, pady=5)
num_total = tk.Entry(form)
num_total.grid(row=3, column=1, padx=10, pady=5)
num_total = tk.Entry(form, textvariable=quantidade)


form.mainloop()