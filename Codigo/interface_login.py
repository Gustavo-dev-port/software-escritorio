import customtkinter as ctk
import sqlite3
import os
from tkinter import messagebox

caminho_banco = os.path.join('..', 'banco_de_dados', 'advocacia.db')

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela de Listagem de Usuários
class janelaListagem(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Lista de Usuários")
        self.geometry("700x500")
        self.grab_set()  # Garante que a janela seja modal

        self.label_titulo = ctk.CTkLabel(self, text="Usuários Cadastrados", font=("Roboto", 20, "bold"))
        self.label_titulo.pack(pady=20)

        #Criando o frame com rolagem
        self.frame_lista = ctk.CTkScrollableFrame(self, width=650, height=350)
        self.frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        self.criar_cabecalho()

        self.carregar_usuarios()

    def criar_cabecalho(self):
        head_frame = ctk.CTkFrame(self.frame_lista, fg_color="transparent")
        head_frame.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(head_frame, text="Nome", width=200, font=("Roboto", 12, "bold")).grid(row=0, column=0, padx=5)
        ctk.CTkLabel(head_frame, text="CPF", width=150, font=("Roboto", 12, "bold")).grid(row=0, column=1, padx=5)  
        ctk.CTkLabel(head_frame, text="Hierarquia", width=150, font=("Roboto", 12, "bold")).grid(row=0, column=2, padx=5)
        ctk.CTkLabel(head_frame, text="Data de Admissão", width=150, font=("Roboto", 12, "bold")).grid(row=0, column=3, padx=5)
        ctk.CTkLabel(head_frame, text="Situação", width=100, font=("Roboto", 12, "bold")).grid(row=0, column=4, padx=5)
        ctk.CTkLabel(head_frame, text="Data de Demissão", width=150, font=("Roboto", 12, "bold")).grid(row=0, column=5, padx=5)
        ctk.CTkLabel(head_frame, text="Email", width=200, font=("Roboto", 12, "bold")).grid(row=0, column=6, padx=5)


    def carregar_usuarios(self):

        for widget in self.frame_lista.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and widget != self.frame_lista.winfo_children()[0]:  # Ignora o cabeçalho
                widget.destroy()

        try:
            conexao = sqlite3.connect(caminho_banco)
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, cpf, hierarquia, data_admissao, situacao, data_demissao, email FROM usuarios")
            usuarios = cursor.fetchall()

            for user in usuarios:
                id, nome, cpf, hierarquia, data_admissao, situacao, data_demissao, email = user
                
                linha = ctk.CTkFrame(self.frame_lista)
                linha.pack(fill="x", padx=5, pady=2)

                ctk.CTkLabel(linha, text=id, width=50).grid(row=0, column=0, padx=5)
                ctk.CTkLabel(linha, text=nome, width=200).grid(row=0, column=0, padx=5)
                ctk.CTkLabel(linha, text=cpf, width=150).grid(row=0, column=1, padx=5)
                ctk.CTkLabel(linha, text=hierarquia, width=150).grid(row=0, column=2, padx=5)
                ctk.CTkLabel(linha, text=data_admissao, width=150).grid(row=0, column=3, padx=5)
                ctk.CTkLabel(linha, text=situacao, width=100).grid(row=0, column=4, padx=5)
                ctk.CTkLabel(linha, text=data_demissao, width=150).grid(row=0, column=5, padx=5)
                ctk.CTkLabel(linha, text=email, width=200).grid(row =0, column=6, padx=5)

                btn_excluir = ctk.CTkButton(linha, text="🗑️", fg_color="red", hover_color="darkred", command=lambda i=id, n=nome: self.excluir_usuario(i, n))
                btn_excluir.grid(row=0, column=7, padx=5)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar os usuários: {e}")
        finally:
            if 'conexao' in locals():
                conexao.close()
    
    def excluir_usuario(self, id_user, nome):
        resposta = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o usuário '{nome}'?")
        if resposta:
            try:
                conexao = sqlite3.connect(caminho_banco)
                cursor = conexao.cursor()
                cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_user,))
                conexao.commit()
                messagebox.showinfo("Sucesso", f"Usuário '{nome}' excluído com sucesso!")
                self.carregar_usuarios()  # Atualiza a lista após exclusão
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao excluir o usuário: {e}")
            finally:
                if 'conexao' in locals():
                    conexao.close()



# Janela Pop-up de cadastro de usuário
class janelaCadastro(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title("Cadastro de Usuário")
        self.geometry("400x500")
        self.grab_set()  # Garante que a janela seja modal

        self.label_titulo = ctk.CTkLabel(self, text="Novo Usuário", font=("Roboto", 20))
        self.label_titulo.pack(pady=20)

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome Completo")
        self.entry_nome.pack(pady=10)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack(pady=30)

        self.entry_cpf = ctk.CTkEntry(self, placeholder_text="CPF")
        self.entry_cpf.pack(pady=10)

        #menu de opção de hierarquia
        self.label_h = ctk.CTkLabel(self, text="Nivel de Acesso:")
        self.label_h.pack(pady=5)
        self.combo_hierarquia = ctk.CTkComboBox(self, values=["Comum", "Administrador"])
        self.combo_hierarquia.pack(pady=10)

        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=250)
        self.entry_senha.pack(pady=10)

        self.botao_cadastrar = ctk.CTkButton(self, text="Cadastrar", command=self.cadastrar_usuario, fg_color="green", hover_color="darkgreen")
        self.botao_cadastrar.pack(pady=30)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        cpf = self.entry_cpf.get().strip()
        hierarquia = self.combo_hierarquia.get().strip()
        senha_hash = self.entry_senha.get().strip()

        if not nome or not email or not cpf or not hierarquia or not senha_hash:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            conexao = sqlite3.connect(caminho_banco)
            cursor = conexao.cursor()

            cursor.execute("SELECT id FROM usuarios WHERE cpf = ?", (cpf,))
            if cursor.fetchone():
                messagebox.showerror("Erro", "CPF já cadastrado. Por favor, use um CPF diferente.")
                return

            cursor.execute("INSERT INTO usuarios (nome, email, cpf, hierarquia, senha_hash) VALUES (?, ?, ?, ?, ?)", 
                           (nome, email, cpf, hierarquia, senha_hash))
            conexao.commit()

            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.destroy()  # Fecha a janela de cadastro após o sucesso
        
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro ao cadastrar o usuário: {e}")
        finally:
            if 'conexao' in locals():
                conexao.close()


class Dashboard(ctk.CTk):
    def __init__(self, usuario_nome, usuario_hierarquia):
        super().__init__()
        self.title("Sistema de Advocacia -- Menu Principal")
        self.geometry("600x400")
        self.resizable(False, False)

        # Barra Lateral
        self.label_bem_vindo = ctk.CTkLabel(self, text=f"Bem-vindo, {usuario_nome}!", font=("Roboto", 18))
        self.label_bem_vindo.pack(pady=20)

        # Container para os botões
        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.pack(pady=20, padx=20, fill="both", expand=True)

        # Botao para cadastrar usuário (apenas para hierarquia "Administrador")
        if usuario_hierarquia == "Administrador" or usuario_hierarquia == "Advogado":
            self.botao_cadastrar_usuario = ctk.CTkButton(self.frame_botoes, text="Cadastrar Usuário", command=self.abrir_janela_cadastro, width=200, height=50)
            self.botao_cadastrar_usuario.grid(row=0, column=0, padx=20, pady=20)

            self.botao_listar_usuarios = ctk.CTkButton(self.frame_botoes, text="Listar Usuários", command=self.listar_usuarios, width=200, height=50)
            self.botao_listar_usuarios.grid(row=0, column=1, padx=20, pady=20)
        else:
            self.label_info = ctk.CTkLabel(self.frame_botoes, text="Acesso restrito. Contate o administrador para mais opções.", font=("Roboto", 14))
            self.label_info.pack(pady=50)

    def abrir_janela_cadastro(self):
        self.janela_cad = janelaCadastro(self)
    
    def listar_usuarios(self):
        self.listar_usuarios = janelaListagem(self)
        


class JanelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Sistema de Advocacia")
        self.geometry("400x350")
        self.resizable(False, False)

        self.label_cpf = ctk.CTkLabel(self, text="CPF:")
        self.label_cpf.pack(pady=10)
        self.entry_cpf = ctk.CTkEntry(self)
        self.entry_cpf.pack(pady=5)

        self.label_senha = ctk.CTkLabel(self, text="Senha:")
        self.label_senha.pack(pady=10)
        self.entry_senha = ctk.CTkEntry(self, show="*")
        self.entry_senha.pack(pady=5)

        self.botao_login = ctk.CTkButton(self, text="Login", command=self.login)
        self.botao_login.pack(pady=20)

    def validar_login(self):
        cpf = self.entry_cpf.get()
        senha_hash = self.entry_senha.get()
        if not cpf or not senha_hash:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return False
        return True

    def login(self):
        if not self.validar_login():
            return
        
        cpf = self.entry_cpf.get()
        senha_hash = self.entry_senha.get()
        
        try:
            conexao = sqlite3.connect(caminho_banco)
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, hierarquia FROM usuarios WHERE cpf = ? AND senha_hash = ?", (cpf, senha_hash))
            usuario = cursor.fetchone()
            if usuario:
                nome_logado = usuario[1]
                hierarquia_logado = usuario[2]
                self.destroy()  # Fecha a janela de login
                dashboard = Dashboard(nome_logado, hierarquia_logado)
                dashboard.mainloop()  # Abre a janela do dashboard
            else:
                messagebox.showerror("Erro", "CPF ou senha incorretos. Tente novamente.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante o login: {e}")
        finally:
            if 'conexao' in locals():
                conexao.close()


if __name__ == "__main__":
    app = JanelaLogin()
    app.mainloop()