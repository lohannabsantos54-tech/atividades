import sys
from database.connection import init_db
from modules.auth import criar_usuario

def main():
    print("Iniciando o Sistema de Vendas...")

    # 1. Inicializa o banco de dados (cria as tabelas se não existirem)
    init_db()

    # 2. Cria o usuário administrador padrão caso o banco esteja vazio
    criar_usuario_admin_padrao()

    print("\n" + "="*30)
    print("     SISTEMA DE VENDAS v1.0")
    print("="*30)

    # Loop de login
    while True:
        print("\n--- LOGIN ---")
        login = input("Usuário: ")
        senha = input("Senha: ")

        sucesso, msg = autenticar_usuario(login, senha)

        if sucesso:
            print(f"\n[SUCESSO] {msg}")
            menu_principal()
            break
        else:
            print(f"\n[ERRO] {msg}")
            tentar_novamente = input("Deseja tentar novamente? (S/N): ").strip().lower()
            if tentar_novamente == 'n':
                print("Encerrando o sistema...")
                sys.exit(0)

def menu_principal():
    while True:
        print("\n" + "="*30)
        print("         MENU PRINCIPAL")
        print("="*30)
        print(f"Usuário Logado: {Session.nome} | Cargo: {Session.cargo}")
        print("-" * 30)
        print("1. Cadastrar Produto (Em breve)")
        print("2. Nova Venda (Em breve)")
        print("3. Relatórios (Em breve)")