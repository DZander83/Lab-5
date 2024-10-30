import csv
import json
#no se puede usar libreria CSV, leer como archivo de texto
def cargar_usuarios(ruta_archivocsv):
    usuarios = []
    with open(ruta_archivocsv, mode='r') as archivo_csv:
        lector_csv=archivo_csv.read()
        for fila in lector_csv:
            usuarios.append(fila)
    return usuarios

def verificar_login(codigo, clave, usuarios):
    for usuario in usuarios:
        if usuario['codigo'] == codigo and usuario['clave'] == clave:
            if usuario['rol']==Administrador:
                seluser=0
                return seluser
            if usuario['rol']==Operador:
                seluser=1
                return seluser
            return True
            
            
    return False

ruta_archivocsv = 'usuarios.csv' 
ruta_archivojson = 'registros.json' 

usuarios = cargar_usuarios(ruta_archivocsv)

codigo_ingresado = input("Ingrese su documento: ")
clave_ingresada = input("Ingrese su clave: ")
resultado = verificar_login(codigo_ingresado, clave_ingresada, usuarios)

def cargar_datos_json():
    datos_clima = []
    with open("registros.json", mode='r') as archivo_json:
        datos_clima = json.load(archivo_json)
    return datos_clima
