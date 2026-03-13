import cadastrar_usuario
import listar_usuarios
import login
import os

def menu():
    logado = login.login()  
    if logado == True:  # Tenta fazer login antes de mostrar o menu
        input("Login Autorizado! Pressione Enter para continuar...")  # Pausa para o usuário ler a mensagem de login
        while True:

            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para melhor visualização
            print("\n---- Menu Principal ----")
            print("1. Cadastrar Usuário")
            print("2. Listar Usuários")
            print("3. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                cadastrar_usuario.cadastrar_usuario()
            elif escolha == '2':
                listar_usuarios.listar_usuarios()
            elif escolha == '3':
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    else:
        print("Login falhou. Encerrando o programa...")
        input("Pressione Enter para sair...")  # Pausa para o usuário ler a mensagem de falha no login

if __name__ == "__main__":
    menu()