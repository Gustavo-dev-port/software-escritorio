
import sqlite3
import os

# Caminho Banco de dados
caminho_banco = os.path.join('..', 'banco_de_dados', 'advocacia.db') 



def login():
    print("---- Login ----")
    cpf = input("CPF: ")
    senha_hash = input("Senha: ")

    try:
        conexao = sqlite3.connect(caminho_banco)
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, hierarquia FROM usuarios WHERE cpf = ? AND senha_hash = ?", (cpf, senha_hash))
        usuario = cursor.fetchone()
        if usuario:
            print(f"Login bem-sucedido! Bem-vindo, {usuario[1]} ({usuario[2]})!")
            return True  # Retorna os dados do usuário logado
        else:
            print("Email ou senha incorretos. Tente novamente.")
            return False
    except Exception as e:
        print(f"Ocorreu um erro durante o login: {e}")
        return None
    finally:
        conexao.close()

if __name__ == "__main__":
    login()