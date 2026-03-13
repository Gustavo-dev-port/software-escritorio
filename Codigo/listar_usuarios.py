import sqlite3
import os

caminho_banco = os.path.join('..', 'banco_de_dados', 'advocacia.db')
def listar_usuarios():
    print("---- Lista de Usuários ----")
    try:
        conexao = sqlite3.connect(caminho_banco)
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, cpf, hierarquia, data_admissao, situação, data_demissao, email FROM usuarios")
        usuarios = cursor.fetchall()
        if usuarios:
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nome: {usuario[1]}, CPF: {usuario[2]}, Hierarquia: {usuario[3]}, Data de Admissão: {usuario[4]}, Situação: {usuario[5]}, Data de Demissão: {usuario[6]}, Email: {usuario[7]}")
        else:
            print("Nenhum usuário encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao listar os usuários: {e}")
    finally:
        conexao.close()

if __name__ == "__main__":
    listar_usuarios()