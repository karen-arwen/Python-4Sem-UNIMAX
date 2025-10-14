import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Selecionar todos os registros da tabela alunos
cursor.execute('SELECT * FROM alunos')
alunos = cursor.fetchall()

# Mostrar os dados dos alunos
for aluno in alunos:
    print(f"RA: {aluno[0]}, Nome: {aluno[1]}, Endereço: {aluno[2]}, Cidade: {aluno[3]}, Estado: {aluno[4]}, Celular: {aluno[5]}, Email: {aluno[6]}")

conn.close()