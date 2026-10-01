import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.config(bg="#BD53C3")

janela.geometry('300x500')
janela.resizable(False,False)

janela.title("Login")

titulo = tk.Label(text="Login", font=("Arial", 18, "bold"), bg="#6A1B60", fg="#C050C8")
titulo.place(rely=0.1, relx=0.5, anchor='center')

labelUser = tk.Label(text="Insira seu nome", bg="#B550AB", fg="#DB73CD")
labelUser.place(rely=0.33, relx=0.5, anchor="center")

entraUser = tk.Entry()
entraUser.place(rely=0.45, relx=0.5, anchor='center')

labelSenha = tk.Label(text="Insira sua senha", bg="#83458F", fg="#BC7AC2")
labelSenha.place(rely=0.60, relx=0.5, anchor='center')

entraSenha = tk.Entry()
entraSenha.place(rely=0.72, relx=0.5, anchor='center')

def checklogin():
    nome = entraUser.get()
    senha = entraSenha.get()
    if nome == "margarida" and senha ==" 1234 ":
        novjanela = tk.Toplevel()
        novjanela.config(bg="#CD8AD9")
        novjanela.resizable(False, False)
        novjanela.geometry('800x600')
    else:
        messagebox.showerror("Erro", "Nome ou senha incorretos(a),Tente novamente!!!")


butLogin = tk.Button(text="Entrar", bg="#8142A3", fg="#AE58A6", command=checklogin)
butLogin.place(rely=0.9, relx=0.5, anchor='center')

janela.mainloop()




