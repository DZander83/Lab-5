import csv
import json
from datetime import datetime

# ------------------------------
# Lectura y escritura en CSV sin métodos adicionales
# ------------------------------

# Función para leer usuarios desde usuarios.csv
def leer_usuarios():
    ruta_usuarios = "usuarios.csv"
    usuarios = []
    with open(ruta_usuarios, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.read(archivo)
        encabezado = None
        fila_numero = 0
        for fila in lector_csv:
            if fila_numero == 0:
                encabezado = []
                for campo in fila:
                    encabezado += [campo]
            else:
                usuario = {}
                if len(fila) == len(encabezado):
                    for i in range(len(encabezado)):
                        clave = encabezado[i]
                        valor = fila[i]
                        usuario[clave] = valor
                    usuarios = usuarios + [usuario]
            fila_numero += 1
    return usuarios

# Función para guardar usuarios en usuarios.csv
def guardar_usuarios(usuarios):
    ruta_usuarios = "usuarios.csv"
    with open(ruta_usuarios, 'w', encoding='utf-8', newline='') as archivo:
        escritor_csv = csv.read(archivo)
        encabezado = ['codigo', 'nombre', 'clave', 'rol']
        escritor_csv.writerow(encabezado)
        for usuario in usuarios:
            fila = []
            for key in encabezado:
                valor = usuario[key] if key in usuario else ""
                fila += [valor]
            escritor_csv.writerow(fila)

# Función para añadir un nuevo usuario
def agregar_usuario(documento, nombre, contraseña, rol):
    usuarios = leer_usuarios()
    nuevo_usuario = {
        'codigo': documento,
        'nombre': nombre,
        'clave': contraseña,
        'rol': rol
    }
    usuarios = usuarios + [nuevo_usuario]
    guardar_usuarios(usuarios)
    print("Usuario agregado exitosamente.")

# Función para editar un usuario
def editar_usuario(identificacion, nuevos_datos):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        if usuario['codigo'] == identificacion:
            for key in nuevos_datos:
                usuario[key] = nuevos_datos[key]
    guardar_usuarios(usuarios)

# Función para eliminar un usuario
def eliminar_usuario(identificacion):
    usuarios = leer_usuarios()
    usuarios = [usuario for usuario in usuarios if usuario['codigo'] != identificacion]
    guardar_usuarios(usuarios)

# ------------------------------
# Lectura y escritura en JSON sin métodos adicionales
# ------------------------------

# Función para leer variables desde variables.json
def leer_variables():
    ruta_variables = "variables.json"
    with open(ruta_variables, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        variables = json.loads(contenido)
    return variables

# Función para guardar variables en variables.json
def guardar_variables(variables):
    ruta_variables = "variables.json"
    with open(ruta_variables, 'w', encoding='utf-8') as archivo:
        archivo.write(json.dumps(variables, indent=4))

# Función para leer registros desde registros.json
def leer_registros():
    ruta_registros = "registros.json"
    with open(ruta_registros, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        registros = json.loads(contenido)
    return registros

# Función para guardar registros en registros.json
def guardar_registros(registros):
    ruta_registros = "registros.json"
    with open(ruta_registros, 'w', encoding='utf-8') as archivo:
        archivo.write(json.dumps(registros, indent=4))

# ------------------------------
# Funciones de manejo de medidas
# ------------------------------

# Función para añadir una medida a registros.json
def agregar_medida(codigo_estacion, variable, valor):
    registros = leer_registros()
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    if codigo_estacion not in registros:
        registros[codigo_estacion] = {}
    if variable not in registros[codigo_estacion]:
        registros[codigo_estacion][variable] = {}
    if fecha_actual not in registros[codigo_estacion][variable]:
        registros[codigo_estacion][variable][fecha_actual] = []
    registros[codigo_estacion][variable][fecha_actual] += [valor]
    guardar_registros(registros)

# Función para editar una medida en registros.json
def editar_medida(codigo_estacion, variable, fecha, nuevos_valores):
    registros = leer_registros()
    if codigo_estacion in registros and variable in registros[codigo_estacion] and fecha in registros[codigo_estacion][variable]:
        registros[codigo_estacion][variable][fecha] = nuevos_valores
    guardar_registros(registros)

# Función para eliminar una medida de registros.json
def eliminar_medida(codigo_estacion, variable, fecha):
    registros = leer_registros()
    if codigo_estacion in registros and variable in registros[codigo_estacion] and fecha in registros[codigo_estacion][variable]:
        del registros[codigo_estacion][variable][fecha]
        if not registros[codigo_estacion][variable]:
            del registros[codigo_estacion][variable]
        if not registros[codigo_estacion]:
            del registros[codigo_estacion]
    guardar_registros(registros)

# ------------------------------
# Verificación de credenciales sin métodos adicionales
# ------------------------------

# Función para verificar usuario y obtener rol sin métodos adicionales
def verificar_credenciales(documento, clave):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        identificacion_correcta = False
        clave_correcta = False
        rol_usuario = None
        
        for key in usuario:
            if key == 'codigo' and usuario[key] == documento:
                identificacion_correcta = True
            if key == 'clave' and usuario[key] == clave:
                clave_correcta = True
            if key == 'rol' and identificacion_correcta and clave_correcta:
                rol_usuario = usuario[key]
                return rol_usuario
                
    return None
# ------------------------------
# Validaciones
# ------------------------------

def validar_nombre(nombre):
    for c in nombre:
        if not ('A' <= c <= 'Z' or 'a' <= c <= 'z' or c == ' '):
            return False
    return True

def validar_documento(documento):
    if len(documento) != 10:
        return False
    for c in documento:
        if not ('0' <= c <= '9'):
            return False
    return True

# Validación de contraseña
def validar_contraseña():
    contraseña1 = input("Ingrese la contraseña: ")
    contraseña2 = input("Confirme la contraseña: ")
    
    if len(contraseña1) >= 4 and contraseña1 == contraseña2:
        return contraseña1
    else:
        print("Error: Las contraseñas no coinciden o tienen menos de 4 caracteres.")
        return None

# ------------------------------
# Visualización de datos
# ------------------------------

# Función para imprimir una tabla
def imprimir_tabla(tabla, ancho, encabezado=None):
    def dividir_fila(ancho, sep='-'):
        linea = ''
        for i in range(len(ancho)):
            linea += '+' + sep * (ancho[i] - 1)
        linea += '+'
        print(linea)

    def imprimir_celda(texto, impresos, relleno):
        texto = str(texto).replace('\n', ' ').replace('\t', ' ')
        texto_len = len(texto)
        if impresos + relleno < texto_len:
            print(texto[impresos:impresos + relleno], end='')
            impresos += relleno
        else:
            print(texto[impresos:], end='')
            print(' ' * (relleno - (texto_len - impresos)), end='')
            impresos = texto_len
        return impresos

    def imprimir_fila(fila):
        impresos = [0] * len(fila)
        alto = max(len(str(celda)) // (ancho[i] - 3) + 1 for i, celda in enumerate(fila))
        for _ in range(alto):
            print('| ', end='')
            for j, celda in enumerate(fila):
                relleno = ancho[j] - 3
                impresos[j] = imprimir_celda(celda, impresos[j], relleno)
                if j == len(fila) - 1:
                    print(' |')
                else:
                    print(' | ', end='')

    if encabezado:
        dividir_fila(ancho, '=')
        imprimir_fila(encabezado)
        dividir_fila(ancho, '=')
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)
