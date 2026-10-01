import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Login")
janela.geometry("300x500")
janela.config(bg="#BD53C3")
janela.resizable(False, False)

tk.Label(janela, text="Login", font=("Arial", 18, "bold"),
         bg="#6A1B60", fg="white").place(rely=.1, relx=.5, anchor="center")

tk.Label(janela, text="Nome", bg="#BD53C3").place(rely=.33, relx=.5, anchor="center")
entraUser = tk.Entry(janela)
entraUser.place(rely=.42, relx=.5, anchor="center")

tk.Label(janela, text="Senha", bg="#BD53C3").place(rely=.55, relx=.5, anchor="center")
entraSenha = tk.Entry(janela, show="*")
entraSenha.place(rely=.64, relx=.5, anchor="center")


def cadastro():
    tela = tk.Toplevel()
    tela.title("Cadastro")
    tela.geometry("350x300")
    tela.config(bg="#CD8AD9")

    entradas = []

    for i, texto in enumerate(["Nome", "CPF", "Telefone"]):
        tk.Label(tela, text=texto, bg="#CD8AD9").place(x=70, y=50+i*50)
        e = tk.Entry(tela)
        e.place(x=130, y=50+i*50)
        entradas.append(e)

    def salvar():
        if all(e.get() for e in entradas):
            messagebox.showinfo("Sucesso", "Cadastro salvo!")
            tela.destroy()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    tk.Button(tela, text="Salvar", command=salvar).place(x=100, y=220)
    tk.Button(tela, text="Cancelar", command=tela.destroy).place(x=190, y=220)


def login():
    if entraUser.get() == "margarida" and entraSenha.get() == "1234":
        tela = tk.Toplevel()
        tela.title("Menu")
        tela.geometry("400x300")
        tela.config(bg="#CD8AD9")

        tk.Label(tela, text="Menu Principal",
                 font=("Arial", 18, "bold"),
                 bg="#CD8AD9").pack(pady=30)

        tk.Button(tela, text="Cadastrar Cliente",
                  command=cadastro).pack()
    else:
        messagebox.showerror("Erro", "Nome ou senha incorretos!")


tk.Button(janela, text="Entrar", command=login).place(
    rely=.8, relx=.5, anchor="center"
)

janela.mainloop()
