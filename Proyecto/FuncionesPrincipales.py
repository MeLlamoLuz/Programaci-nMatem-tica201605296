# -*- coding: utf-8 -*-

import Tkinter as tk

def hacerEntrada(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entrada = tk.Entry(parent, **options)
    if width:
        entrada.config(width=width)
    entrada.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entrada    
