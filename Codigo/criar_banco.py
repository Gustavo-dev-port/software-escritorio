import sqlite3
import os

# caminho do banco de dados
caminho_banco = os.path.join('..', 'banco_de_dados', 'advocacia.db')

# criar conexão com o banco de dados
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    hierarquia TEXT NOT NULL,
    data_admissao DATE,
    situacao BOOLEAN NOT NULL DEFAULT 1,
    data_demissao DATE,
    email TEXT UNIQUE,
    senha_hash TEXT NOT NULL
)''')

conexao.commit()
conexao.close()

print("Banco de dados e tabelas criadas com sucesso!")