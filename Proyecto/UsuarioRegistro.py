# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkconstants import BOTTOM
from operator import contains

def hacerEntrada(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entrada = tk.Entry(parent, **options)
    if width:
        entrada.config(width=width)
    entrada.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entrada

def enter(event):
    revisarPassword()
    
def revisarPassword(failures=[]):
    if (usuario.get(), password.get()) in passwords:
        principal.destroy()
        print('Has ingresado exitosamente')
        return
    else:
        print "Datos incorrectos"
        
def nuevoUsuario():
    principal.destroy()
    registro = tk.Tk()
    registro.geometry('300x160')
    registro.title('Registro de nuevo usuario')
    padre = tk.Frame(registro, padx=10, pady=10)
    padre.pack(fill=tk.BOTH, expand=True)
    usuarioNuevo = hacerEntrada(padre, "Ingresa tu correo:", 16)
    password = hacerEntrada(padre, "Ingresa una contraseña:", 16, show="*")
    b = tk.Button(padre, borderwidth=4, text="Registrarme", width=10, pady=8, command=guardarUsuarios)
    b.pack(side = BOTTOM)
    
def guardarUsuarios(todosusuarios, contrasena):
    archivo = open(todosusuarios, "w")
    nombre = usuarioNuevo.get()
    contrasena = password.get()
    if nombre.__contains__("@") and( usuario.__contains__(".com") or usuario.__contains__(".es")):
        archivo.write(nombre+","+ contrasena + "\\n")
        archivo.close()
    else:
        print "Correo inválido, inténtalo de nuevo."
 
def recuperarUsuarios(todosusuarios):
    usuarios = []
    archivo = open(todos_usuarios, "r")
    for linea in archivo:
        nombre, contrasena = linea.rstrip("\\n").split(",")
        usuarios.append((nombre, contrasena))
    archivo.close()
    return usuarios
       
principal = tk.Tk()

w = 250 
h = 170
ws = principal.winfo_screenwidth() 
hs = principal.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
principal.geometry('%dx%d+%d+%d' % (w, h, x, y))
principal.title('Inicio')
padre = tk.Frame(principal, padx=10, pady=10)
padre.pack(fill=tk.BOTH, expand=True)
usuario = hacerEntrada(padre, "Usuario:", 16)
password = hacerEntrada(padre, "Contraseña:", 16, show="*")
b = tk.Button(padre, borderwidth=4, text="Login", width=10, pady=8, command=revisarPassword)
b.pack(side=tk.LEFT)
password.bind('<Return>', enter)
usuario.focus_set()
nusario = tk.Button(padre, borderwidth=4, text="Crear un nuevo usuario",width=17, pady=8, justify = "center", command=nuevoUsuario)
nusario.pack(side =tk.RIGHT)

padre.mainloop()


password.bind('<Return>', enter)
usuario.focus_set()
padre.mainloop()