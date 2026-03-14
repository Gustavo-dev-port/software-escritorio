import sqlite3
import os

# caminho do banco de dados
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(DIRETORIO_ATUAL, '..','..', 'Banco_de_Dados', 'advocacia.db')


def criar_banco():
    # criar conexão com o banco de dados
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    
    cursor.execute('''
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

    # Tabela de clientes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE,
        telefone TEXT,
        endereco TEXT
    )''')

    # Tabela de processos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS processos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_processo TEXT UNIQUE NOT NULL,
        cliente_id INTEGER NOT NULL,
        empresa_reclamada TEXT,
        descricao TEXT,
        status TEXT NOT NULL DEFAULT 'Em andamento',
        data_abertura DATE,
        data_fechamento DATE,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )''')

    # Tabela de Prazos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prazos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        processo_id INTEGER NOT NULL,
        descricao TEXT NOT NULL,
        data_vencimento DATE NOT NULL,
        status TEXT NOT NULL DEFAULT 'Pendente',
        FOREIGN KEY (processo_id) REFERENCES processos(id)
    )''')

    conexao.commit()
    conexao.close()

    print("Banco de dados atualizado com sucesso!")

if __name__ == "__main__":    
    criar_banco()