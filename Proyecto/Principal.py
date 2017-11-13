# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkconstants import BOTTOM
import tkMessageBox
from FuncionesPrincipales import hacerEntrada

usuarios = []
archivo = open('Usuarios.txt', "r")
for linea in archivo:
    nombre, contrasena = linea.rstrip("\\n").split(",")
    usuarios.append((nombre, contrasena))
archivo.close()

def nuevoUsuario(root):
    root.quit()
    registro = tk.Tk()
    registro.title('Registro de nuevo usuario')
    w = 250 
    h = 170
    ws = registro.winfo_screenwidth() 
    hs = registro.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    registro.geometry('%dx%d+%d+%d' % (w, h, x, y))
    padre = tk.Frame(registro, padx=10, pady=10)
    padre.pack(fill=tk.BOTH, expand=True)
    user = hacerEntrada(padre, "Ingresa tu correo:", 16)
    password = hacerEntrada(padre, "Ingresa una contraseña:", 16, show="*")
    c = tk.Button(padre, borderwidth=4, text="Registrarme", width=10, pady=8, command = guardarUsuarios(user, password))
    c.pack(side = BOTTOM)
    
def guardarUsuarios(user, clave):
    archivo = open('Usuarios.txt', "w")
    nombre = user.get()
    contrasena = clave.get()
    if nombre.__contains__("@") and(nombre.__contains__(".com") or nombre.__contains__(".es")):
        archivo.write(nombre+","+ contrasena + "\\n")
        archivo.close()
        tkMessageBox.showinfo("Te has registrado exitosamente.")
    else:
        tkMessageBox.showinfo("Correo invÃ¡lido, intÃ©ntalo de nuevo.")
        
def revisarUsuario(usuario, password, principal):
    if (usuario.get(), password.get()) in usuarios:
        principal.quit()
        tkMessageBox.showinfo('Has ingresado exitosamente')
        inicio()
    else:
        tkMessageBox.showinfo("Datos incorrectos")
         
def inicio():
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
    usuario = hacerEntrada(padre, "Correo:", 16)
    password = hacerEntrada(padre, "Contraseña:", 16, show="*")
    b = tk.Button(padre, borderwidth=4, text="Ingresar", width=10, pady=8, command=revisarUsuario(usuario, password, principal))
    b.pack(side=tk.LEFT)
    usuario.focus_set()
    nusario = tk.Button(padre, borderwidth=4, text="Crear un nuevo usuario",width=17, pady=8, justify = "center", command = nuevoUsuario(principal))
    nusario.pack(side =tk.RIGHT)
    
    padre.mainloop()

inicio()