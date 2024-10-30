import csv y json as cyj
import DefOperador as DefO
import DefAdministrador as DefA
ruta_archivocsvest = 'estaciones.csv'
ruta_archivocsv = 'usuarios.csv' 
ruta_archivojson = 'registros.json' 
ruta_archivojsonvar = 'variables.json'
print("Elija su tipo de usuario o si desea salir del sistema: ","\n", "1. usuario registrado.","\n", "2. usuario visitante.","\n", "3. salir." )
user=input()

if user == 1:
   usuarios = cargar_usuarios(ruta_archivocsv)
   codigo_ingresado = input("Ingrese su documento: ")
   clave_ingresada = input("Ingrese su clave: ")
   resultado = verificar_login(codigo_ingresado, clave_ingresada, usuarios)
   cyj.cargar_usuarios(ruta_archivocsv)
   cyj.verificar_login(codigo, clave, usuarios)
   if seluser==1:
      DefA.Administrador()
      
   if seluser==1:
      DefO.Operador()
      
   

elif user == 2:
    print("Elija el tiempo en el que desea visualizar las estadisticas:", "\n", "1. Ultimos 7 dias.","\n", "2. Ultimos 30 dias.","\n", "3. Elegir manualmente")
    period=input()
    if period == 1:
        # mostrar datos de los ultimos 7 dias
    elif period == 2:
        # mostrar los datos de los ultimos 30 dias
    elif period == 3:
        input("introduzca una fecha:")
    
    
#modificarlo manual
