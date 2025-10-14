import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS alunos')

conn.commit()
conn.close()

print("Tabela alunos removida!")