# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:08:16 2024

@author: dandr
"""
usuario=print("ingresar Usuario: A, para Visitante. B, para Usuarios. C, para salir del sistema")
if usuario=="A":
    import Usuarios as Users
    
if usuario=="B":
    import Visitante as Visi
    
if usuario=="C":
    #algo para salir del sistema
else:
    print("input incorrecto")
