# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:08:16 2024

@author: dandr
"""
usuario=print("ingresar Usuario: A, para Visitante. B, para Usuario. C, para Administrador. D, para salir deñl sitema")
if usuario=="A":
    import Operador as Operator
    
if usuario=="B":
    import Visitante as Visi
    
if usuario=="C":
    import Administrador as Admin
if usuario=="D":
    #algo para salir del sistema
else:
    print("input incorrecto")