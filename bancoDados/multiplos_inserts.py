import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Inserir estados
estados = [
    ('SP',),
    ('RJ',),
    ('MG',),
    ('RS',),
    ('BA',)
]
cursor.executemany('INSERT INTO estado (nome) VALUES (?)', estados)

# Recuperar ids dos estados para usar nas cidades
cursor.execute('SELECT id, nome FROM estado')
estados_ids = {nome: id for id, nome in cursor.fetchall()}

# Inserir cidades relacionadas a estados
cidades = [
    ('São Paulo', estados_ids['SP']),
    ('Rio de Janeiro', estados_ids['RJ']),
    ('Belo Horizonte', estados_ids['MG']),
    ('Porto Alegre', estados_ids['RS']),
    ('Salvador', estados_ids['BA'])
]
cursor.executemany('INSERT INTO cidade (nome, estado_id) VALUES (?, ?)', cidades)

# Recuperar ids das cidades para usar nos alunos
cursor.execute('SELECT id, nome FROM cidade')
cidades_ids = {nome: id for id, nome in cursor.fetchall()}

# Inserir alunos com nomes de personagens de jogos
alunos = [
    ("Link", "Rua Hyrule, 100", cidades_ids['São Paulo'], "11988889999", "link@jogos.com"),
    ("Mario", "Rua Cogumelo, 200", cidades_ids['Rio de Janeiro'], "21977778888", "mario@jogos.com"),
    ("Lara Croft", "Rua Tomb Raider, 300", cidades_ids['Belo Horizonte'], "31966667777", "lara@jogos.com"),
    ("Geralt", "Rua Witcher, 400", cidades_ids['Porto Alegre'], "51955556666", "geralt@jogos.com"),
    ("Samus", "Rua Metroid, 500", cidades_ids['Salvador'], "71944445555", "samus@jogos.com")
]
cursor.executemany('''
INSERT INTO alunos (nome, endereco, cidade_id, celular, email) VALUES (?, ?, ?, ?, ?)
''', alunos)

conn.commit()
conn.close()

print("Dados inseridos nas tabelas estado, cidade e alunos com sucesso!")