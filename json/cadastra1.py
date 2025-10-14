import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

novo_dado = {
    "nome": "Lara Croft",
    "idade": "40",
    "cidade": "Campinas"
}

dados.append(novo_dado)

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4) 

print(dados)