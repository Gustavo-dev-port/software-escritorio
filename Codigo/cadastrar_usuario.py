import sqlite3
import os

caminho_banco = os.path.join('..', 'banco_de_dados', 'advocacia.db')

def cadastrar_usuario():
    print("---- Cadastro de Usuário ----")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    hierarquia = input("Hierarquia (Advogado, Estagiário, etc.): ")
    data_admissao = input("Data de Admissão (YYYY-MM-DD): ")
    situacao = input("Situação (1 - Ativo, 0 - Inativo): ")
    data_demissao = input("Data de Demissão (YYYY-MM-DD, deixe em branco se não aplicável): ")
    email = input("Email: ") 
    senha_hash = input("Senha (será armazenada como hash): ")

    try:
        conexao = sqlite3.connect(caminho_banco)
        cursor = conexao.cursor()
        comando = ('''
            INSERT INTO usuarios (nome, cpf, hierarquia, data_admissao, situacao, data_demissao, email, senha_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''')
        cursor.execute(comando, (nome, cpf, hierarquia, data_admissao, situacao, data_demissao if data_demissao else None, email, senha_hash))
        conexao.commit()
        print(f"Usuário {nome} cadastrado com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"Erro ao cadastrar usuário: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao.close()

if __name__ == "__main__":
    cadastrar_usuario()