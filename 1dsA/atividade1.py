
import tkinter as tk
from tkinter import messagebox

def criarmensagem():
    tk.messagebox.showinfo(title="Resultado", message=(f"Seu nome é {entradanome.get()} e sua idade é {entradaidade.get()}."))

janela = tk.Tk()
janela.title("Nome e idade")
janela.geometry("400x200")
janela.resizable(False,False)
entradanome= tk.Entry(janela)
entradanome.pack(anchor="center")
entradaidade= tk.Entry(janela)
entradaidade.pack(anchor="center",pady=20)
labelnome=tk.Label(text="Nome:")
labelnome.place(x=50,y=0)
labelidade=tk.Label(text="Idade:")
labelidade.place(x=50,y=40)
botaoconfirmar=tk.Button(bg= "#531497",text="Confirmar", command=criarmensagem)
botaoconfirmar.place(x=160,y=100)
janela.mainloop();