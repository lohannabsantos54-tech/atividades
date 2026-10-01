import tkinter as tk
from tkinter import messagebox
from tkinter import*

def criarmensagem():
    tk.messagebox.showinfo(title="Resultado", message= f"{saudacao.get()},{entradanome.get()}!")

janela = tk.Tk()
janela.title("Nome e idade")
janela.geometry("400x200")
janela.resizable(False,False)
entradanome= tk.Entry(janela)
entradanome.pack(anchor="center")
labelnome=tk.Label(text="Nome:")
labelnome.place(x=50,y=0)

saudacao=StringVar(janela)
saudacao.set("Bom dia")

opcoes=OptionMenu(janela,saudacao,"Bom dia","Boa tarde","Boa noite")
opcoes.pack()

botaoconfirmar= tk.Button(bg = "#f258b4", text="Confirmar", command=criarmensagem)
botaoconfirmar.place(x=160,y=100)
janela.mainloop()
