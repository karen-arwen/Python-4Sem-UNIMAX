import tkinter as tk
import json

# Função para adicionar dados no arquivo JSON
def adicionar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()

    # Abrindo o arquivo JSON e carregando os dados existentes
    try:
        with open('dados.json', 'r') as arquivo:
            dados = json.load(arquivo)  # Carrega os dados já existentes
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []  # Se o arquivo não existir ou estiver vazio, cria uma lista vazia

    # Criando um novo registro para adicionar
    novo_registro = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    # Adicionando o novo registro à lista de dados
    dados.append(novo_registro)

    # Salvando os dados de volta no arquivo JSON
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    # Limpando os campos de entrada
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)

# Criando a janela
root = tk.Tk()
root.title("Cadastro de Clientes")

# Criando os widgets para entrada de dados
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=1, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1)

label_cidade = tk.Label(root, text="Cidade:")
label_cidade.grid(row=2, column=0)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=2, column=1)

# Botão para adicionar dados
botao_adicionar = tk.Button(root, text="Adicionar Cliente", command=adicionar_dados)
botao_adicionar.grid(row=3, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()