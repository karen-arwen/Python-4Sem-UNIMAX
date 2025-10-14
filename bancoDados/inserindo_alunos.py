import sqlite3

# Criar conexão e cursor
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Inserir 5 alunos com nomes de animes
alunos = [
    ("Mickey Mouse", "Rua do Mickey, 123", "Disneyland", "CA", "11911111111", "mickey@disney.com"),
    ("Minnie Mouse", "Rua da Minnie, 456", "Disneyland", "CA", "11922222222", "minnie@disney.com"),
    ("Donald Duck", "Avenida dos Patos, 789", "Duckburg", "FL", "11933333333", "donald@disney.com"),
    ("Goofy", "Rua do Pateta, 321", "Monstro Hills", "CA", "11944444444", "goofy@disney.com"),
    ("Pluto", "Rua do Cão, 654", "Disneyland", "CA", "11955555555", "pluto@disney.com")
]

cursor.executemany(''' 
    INSERT INTO alunos (nome, endereco, cidade, estado, celular, email) 
    VALUES (?, ?, ?, ?, ?, ?) 
''', alunos)


# Salvar e fechar
conn.commit()
conn.close()

print("Tabela criada e 5 alunos inseridos com sucesso!")