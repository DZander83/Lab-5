import json

def validar_nombre(nombre):
   
    for caracter in nombre:
       
        if not (caracter.isalpha() or caracter.isspace()):
            return False
    
    return True
   
def validar_documento(documento):
    
    return len(documento) == 10 and documento.isdigit()
    
def validar_fecha(fecha):
    
    if len(fecha) != 10:
        return False
    if fecha[4] != '-' or fecha[7] != '-':
        return False

    año_str= fecha[:4] 
    mes_str= fecha[5:7]
    dia_str= fecha[8:]
    
    if not (año_str.isdigit() and mes_str.isdigit() and dia_str.isdigit()):
        return False

    año = int(año_str)
    mes = int(mes_str)
    dia = int(dia_str)
    
    if mes < 1 or mes > 12:
        return False

    dias_por_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    
    if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) and mes == 2:
        dias_por_mes[2] = 29

    if dia < 1 or dia > dias_por_mes[mes]:
        return False

    return True


def limpiar_pantalla():
    
    return print('\n'*20)

def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
    '''
    def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        se: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)
        
    def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        # Imprimir celda
        if type(texto) == type(0.0):
            #print(texto)
            texto = '{:^7.2f}'.format(texto)
            #print(type(texto), texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
    def imprimir_fila(fila):
        '''
        fila: Lista con los textos de las celdas de la fila
        '''
        impresos = []   
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto)//(ancho[i]-4)
            if len(texto)%(ancho[i]-4) != 0:
                alto1+=1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            print('| ',end='')
            for j in range(len(fila)):
                relleno = ancho[j]-3
                if j == len(fila)-1:
                    relleno = ancho[j] -4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' |')
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' | ',end='')   
    if not len(tabla) > 0:
        return
    if not type(tabla[0]) is list:
        return
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho+3]*ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i]+=3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado != None:
        dividir_fila(ancho,'=')
        imprimir_fila(encabezado)
        dividir_fila(ancho,'=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)

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
def Admin()
print("1: para gestionar estaciones.","\n", " 2: para gestionar usuarios.","\n", " 3. para volver al menu")
Opciones=input()
if Opciones=="1":
   print("1: para crear una estacion.","\n", "2: para eliminar una estacion.","\n", " 3: para elegir una estacion.")
   GestionEstaciones=input()
if Opciones=="2":
   print("1: para crear un usuario.","\n", "2: para editar un usuario.","\n", "para eliminar un usuario")
   GestionUsuarios=input()
if Opciones=="3":
   #algo para que vuelva al menu
  
   
def Operador()
print("1: para seleccionar una estacion.","\n", " 2. para volver al menu")
Opciones=input()
if Opciones=="1":

elif Opciones=="2":
