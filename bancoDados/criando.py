import sqlite3

# Conectar (ou criar) o banco escola.db
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Criar tabela alunos com os campos especificados
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    ra INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    celular TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Tabela alunos criada com sucesso!")