ARQUIVO= "cadastros.txt" 

def cadastrar_usuario():
    nome=input("Digite o nome:").strip() 
    email=input("Digite o e-mail:").strip()
    telefone=input("Digite o telefone:").strip()

    if not nome or not email:
     print("Erro:Nome e E-mail são obrigatórios.")
     return

    with open(ARQUIVO,"a",encoding="utf=8") as f:
       f.write(f"{nome};{email};{telefone}\n")
    print(f"Usuário {nome} cadastrado com sucesso!")

def listar_usuarios():
    try: 
      with open(ARQUIVO,"r",encoding="utf-8") as f:
         linhas=f.readlines()
         if not linhas:
            print("Nenhum cadastro encontrado.")
            return
         
         print("\n---Usuários Cadastrados---")

         for i,linha in enumerate(linhas,1):
          dados=linha.strip().split(";")
          if len(dados)==3:
             nome,email,telefone=dados
             print(f"{i}. Nome: {nome} | E-mail: {email} | Tel:{telefone}")
    except FileNotFoundError:
      print("Arquivo de registros ainda não existe.Faça um cadastro primiero.")

def menu():
   while True:
      print("\n===SISTEMA DE CADASTRO===")
      print("1.Cadastrar usuário")
      print("2.Listar Cadastros")
      print("3.Sair")

      