import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

query = '''
SELECT a.ra, a.nome, a.endereco, c.nome as cidade, e.nome as estado, a.celular, a.email
FROM alunos a
JOIN cidade c ON a.cidade_id = c.id
JOIN estado e ON c.estado_id = e.id
WHERE e.nome = 'SP'
'''

cursor.execute(query)
alunos_sp = cursor.fetchall()

for aluno in alunos_sp:
    print(f"RA: {aluno[0]}, Nome: {aluno[1]}, Endereço: {aluno[2]}, Cidade: {aluno[3]}, Estado: {aluno[4]}, Celular: {aluno[5]}, Email: {aluno[6]}")

conn.close()