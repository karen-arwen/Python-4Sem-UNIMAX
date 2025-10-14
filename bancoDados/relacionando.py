import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Criar tabela estado
cursor.execute('''
CREATE TABLE IF NOT EXISTS estado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL
)
''')

# Criar tabela cidade com foreign key para estado
cursor.execute('''
CREATE TABLE IF NOT EXISTS cidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    estado_id INTEGER NOT NULL,
    FOREIGN KEY (estado_id) REFERENCES estado(id)
)
''')

# Criar tabela alunos com foreign key para cidade
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    ra INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    cidade_id INTEGER NOT NULL,
    celular VARCHAR(20) NOT NULL,
    email VARCHAR(150) NOT NULL,
    FOREIGN KEY (cidade_id) REFERENCES cidade(id)
)
''')

conn.commit()
conn.close()
print("Tabelas criadas com relacionamentos!")