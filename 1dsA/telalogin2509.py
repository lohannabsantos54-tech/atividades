import hashlib
import os
import sqlite3
from tkinter import messagebox

def init_db():
 with sqlite3.connect("sistema.db") as conn:
  cursor = conn.cursor()
  cursor.execute ("""
CREATE TABLE IF NOT EXISTS usuarios (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 usarname TEXT UNIQUE NOT NULL,
 salt BLOB NOT NULL,
 hash_senha BLOB NOT NULL
)
""")
  conn.commit()

  def hash_senha(senha:str,salt: bytes =None) -> tuple[bytes,bytes]:
   if salt is None:
    salt = os.urandom(16)
    chave=haslib.pbkdf2_hmac(
     hash_name="sha256",
     password=senha.encode("utf-8"),
     salt=salt,
     iterations=100_100
    )
   return salt,chave

  def cadastrar_usuario(username: str,senha:str)->tuple[bool,str]:
   if not username.strip() or not senha.strip():
    return False,"Usuário e senha não podem estar vazios."
   Salt,senha_hasheada=hash_senha(senha)
   try:
    with sqlite3.connect("sistema.db") as conn:
     cursor=conn.cursor()
     cursor.execute(
      "INSERT INTO usuarios(username,salt,hash_senha) VALUES (?,?,?)",
      (username.strip(), salt ,senha_hasheada)
     )
     conn.commit()
     return True,"Usuário cadastrado com sucesso!"
   except sqlite3.IntegrityError:
    return False ,"Nome de Usuário já existe no sistem." 
   except Exception as e:
    return False,f"Erro ao cadastrar: {e}"

   def autenticar_usuario(username:str, senha: str) -> bool:
    with sqlite3.connect("sistema.db") as conn:
     cursor = conn.cursor()
     cursor.execute(
      "SELECT salt,hash_senha FROM usuarios WHERE username=?",
      (username.strip(),)
     )
  registro = cursor.fetchone()
  if not registro:
   salt,hash_gravado=registro
  _,hash_calculado = hash_senha( senha,salt)      
  return hash_calculado== hash_gravado

 class SistemaLogin:
  def _init_(self,root:tk.Tk):
   self.root=root
 self.root.title("Acesso ao Sistema")
 self.root.geometry("380x400")
 self.root.resizable(False,False)
 self.container=tk.Frame(self.root,padx=24,pady=24)
 


