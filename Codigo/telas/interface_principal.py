import customtkinter as ctk

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
        if usuario_hierarquia == "Administrador":
            self.botao_cadastrar_usuario = ctk.CTkButton(self.frame_botoes, text="Cadastrar Usuário", command=self.cadastrar_usuario, width=200, height=50)
            self.botao_cadastrar_usuario.grid(row=0, column=0, padx=20, pady=20)

        # Botao para listar usuários (apenas para hierarquia "Administrador")
        if usuario_hierarquia == "Administrador":
            self.botao_listar_usuarios = ctk.CTkButton(self.frame_botoes, text="Listar Usuários", command=self.listar_usuarios, width=200, height=50)
            self.botao_listar_usuarios.grid(row=0, column=1, padx=20, pady=20)
        
        # Botao para sair do sistema
        self.botao_sair = ctk.CTkButton(self.frame_botoes, text="Sair", fg_color="red", hover_color="darkred", command=self.sair)
        self.botao_sair.pack(pady=20)

        def cadastrar_usuario(self):
            print("Função de cadastrar usuário chamada")

        def listar_usuarios(self):
            print("Função de listar usuários chamada")

        if __name__ == "__main__":
            dashboard = Dashboard("Usuário Exemplo", "Administrador")
            dashboard.mainloop()