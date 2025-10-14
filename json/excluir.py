import json

def excluir_pessoa(nome_excluir):
    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)

    dados_atualizados = [pessoa for pessoa in dados if pessoa['nome'].lower() != nome_excluir.lower()]

    with open('dados.json', 'w') as arquivo:
        json.dump(dados_atualizados, arquivo, indent=4)

    return len(dados) != len(dados_atualizados)  # Retorna True se alguma pessoa foi removida

nome = input("Digite o nome da pessoa para excluir: ")
if excluir_pessoa(nome):
    print("Pessoa excluída com sucesso.")
else:
    print("Pessoa não encontrada.")