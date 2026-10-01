port tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.config(bg="#2B2C2D")
    
janela.geometry('400x200')
janela.resizable(False, False)

janela.title("Login")

titulo = tk.Label(text="Login", font=("Arial", 18, "bold"), bg="#2B2C2D", fg="#FFFFFF")
titulo.place(rely=0.1, relx=0.5, anchor='center')

labelUser = tk.Label(text="Insira seu nome", bg="#2B2C2D", fg="#FFFFFF")
labelUser.place(rely=0.33, relx=0.5, anchor="center")

entraUser = tk.Entry()
entraUser.place(rely=0.45, relx=0.5, anchor='center')

labelSenha = tk.Label(text="Insira sua senha", bg="#2B2C2D", fg="#FFFFFF")
labelSenha.place(rely=0.60, relx=0.5, anchor='c')

entraSenha = tk.Entry()
entraSenha.place(rely=0.72, relx=0.5, anchor='center')

def checklogin():
    nome = entraUser.get()
    senha = entraSenha.get()
    if nome == "admin" and senha == "1234":
        novjanela = tk.Toplevel()
        novjanela.config(bg='#2B2C2D')
        novjanela.resizable(False, False)
        novjanela.geometry('800x600')
    else:
        messagebox.showerror("Erro", "Nome e/ou senha incorreto(a)")

butLogin = tk.Button(text="Entrar", bg="#2B2C2D", fg="#FFFFFF", command=checklogin)
butLogin.place(rely=0.9, relx=0.5, anchor='c')

janela.mainloop()
