import json

def buscar_pessoa(nome_pesquisado):
    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)

    for pessoa in dados:
        if pessoa['nome'].lower() == nome_pesquisado.lower():
            return pessoa
    return None

nome = input("Digite o nome da pessoa: ")

pessoa_encontrada = buscar_pessoa(nome)

if pessoa_encontrada:
    print(f"Nome: {pessoa_encontrada['nome']}")
    print(f"Idade: {pessoa_encontrada['idade']}")
    print(f"Cidade: {pessoa_encontrada['cidade']}")
else:
    print("Nome não encontrado.")