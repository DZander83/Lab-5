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
    
def cargar_estaciones(ruta_archivocsvest):
    estaciones = []
    with open(ruta_archivocsvest, mode='r') as archivo_csv:
        lector_csv=archivo_csv.read()
        for fila in lector_csv:
            estaciones.append(fila)
    return estaciones
    
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
ruta_archivocsvest = 'estaciones.csv'
ruta_archivocsv = 'usuarios.csv' 

usuarios = cargar_usuarios(ruta_archivocsv)

codigo_ingresado = input("Ingrese su documento: ")
clave_ingresada = input("Ingrese su clave: ")
resultado = verificar_login(codigo_ingresado, clave_ingresada, usuarios)

def cargar_datos_json():    #hasta el momento solo abre el json, ver o modificar la informacion se tiene que hacer con otra funcion
    datos_clima = []
    with open("registros.json", mode='r') as archivo_json:
        datos_clima = json.load(archivo_json)
    return datos_clima

def cargar_datos_variables(): 
    clima_variables = []
    with open("variables.json", mode='r') as variables_json:
        clima_variables = json.load(variables_json)
    return clima_variables
