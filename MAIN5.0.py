import funciones

def menu_principal():
    print("\n--- Sistema de Monitoreo de Clima ---")
    print("1. Usuario Registrado")
    print("2. Usuario Visitante")
    print("3. Salir del Sistema")
    opcion = input("Seleccione una opción: ")
    return opcion

def menu_operador():
    print("\n--- Menú Operador ---")
    print("1. Seleccionar estación para ver medidas")
    print("2. Ingresar medidas")
    print("3. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

def menu_administrador():
    print("\n--- Menú Administrador ---")
    print("1. Gestionar estaciones")
    print("2. Gestionar usuarios")
    print("3. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

def menu_visitante():
    print("\n--- Menú Visitante ---")
    print("1. Visualizar estadísticas")
    print("2. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

def seleccionar_periodo():
    print("\n○ Elegir el periodo de tiempo a evaluar:")
    print("1. Últimos 7 días")
    print("2. Últimos 30 días")
    print("3. Elegir fechas manualmente")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función principal
def iniciar_programa():
    while True:
        opcion = menu_principal()

        if opcion == '1':  # Usuario registrado
            documento = input("Ingrese su identificación (código): ")
            clave = input("Ingrese su contraseña: ")

            # Verificar si el usuario existe y obtener su rol
            rol = funciones.verificar_credenciales(documento, clave)

            if rol == 'Administrador':
                while True:
                    opcion_administrador = menu_administrador()
                    if opcion_administrador == '1':
                        print("\n--- Gestión de Estaciones ---")
                        codigo_estacion = input("Ingrese el código de la estación: ")
                        accion = input("Seleccione acción (ver/ingresar/editar/eliminar): ").strip().lower()
                        
                        if accion == 'ver':
                            funciones.mostrar_medidas(codigo_estacion)
                        elif accion == 'ingresar':
                            variable = input("Ingrese la variable (ejemplo: temperatura): ")
                            valor = input("Ingrese el valor de la medida: ")
                            try:
                                valor = float(valor)
                                funciones.agregar_medida(codigo_estacion, variable, valor)
                            except ValueError:
                                print("Valor de medida no válido. Debe ser un número.")
                        elif accion == 'editar':
                            variable = input("Ingrese la variable a editar: ")
                            fecha = input("Ingrese la fecha (yyyy-mm-dd): ")
                            nuevos_valores = input("Ingrese los nuevos valores separados por comas: ").split(',')
                            nuevos_valores = [float(v.strip()) for v in nuevos_valores]
                            funciones.editar_medida(codigo_estacion, variable, fecha, nuevos_valores)
                        elif accion == 'eliminar':
                            variable = input("Ingrese la variable a eliminar: ")
                            fecha = input("Ingrese la fecha (yyyy-mm-dd): ")
                            funciones.eliminar_medida(codigo_estacion, variable, fecha)
                        else:
                            print("Acción no reconocida.")
                        
                    elif opcion_administrador == '2':
                        print("\n--- Gestión de Usuarios ---")
                        accion = input("Seleccione acción (agregar/editar/eliminar): ").strip().lower()
                        
                        if accion == 'agregar':
                            usuarios = funciones.leer_usuarios()
                            while True:
                                documento = input("Ingrese el documento (10 dígitos): ")
                                if not funciones.validar_documento(documento):
                                    print("Error: El documento debe contener exactamente 10 dígitos numéricos.")
                                elif any(usuario['codigo'] == documento for usuario in usuarios):
                                    print("Error: Ya existe un usuario con este documento.")
                                else:
                                    break
                            
                            while True:
                                nombre = input("Ingrese el nombre completo: ")
                                if not funciones.validar_nombre(nombre):
                                    print("Error: El nombre solo debe contener letras y espacios.")
                                else:
                                    break
                            
                            contraseña = None
                            while contraseña is None:
                                contraseña = funciones.validar_contraseña()
                            
                            while True:
                                rol = input("Ingrese el rol (Administrador u Operador): ").capitalize()
                                if rol not in ["Administrador", "Operador"]:
                                    print("Error: El rol debe ser 'Administrador' o 'Operador'.")
                                else:
                                    break
                            funciones.agregar_usuario(documento, nombre, contraseña, rol)
                            
                        elif accion == 'editar':
                            identificacion = input("Ingrese el código del usuario a editar: ")
                            nuevos_datos = {}
                            if input("¿Editar nombre? (s/n): ").strip().lower() == 's':
                                nuevos_datos['nombre'] = input("Nuevo nombre: ")
                            if input("¿Editar clave? (s/n): ").strip().lower() == 's':
                                nuevos_datos['clave'] = funciones.validar_contraseña()
                            if input("¿Editar rol? (s/n): ").strip().lower() == 's':
                                nuevos_datos['rol'] = input("Nuevo rol (Administrador/Operador): ")
                            funciones.editar_usuario(identificacion, nuevos_datos)
                        elif accion == 'eliminar':
                            identificacion = input("Ingrese el código del usuario a eliminar: ")
                            funciones.eliminar_usuario(identificacion)
                        else:
                            print("Acción no reconocida.")
                        
                    elif opcion_administrador == '3':
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                
            elif rol == 'Operador':
                while True:
                    opcion_operador = menu_operador()
                    if opcion_operador == '1':
                        codigo_estacion = input("Ingrese el código de la estación: ")
                        funciones.mostrar_medidas(codigo_estacion)
                    elif opcion_operador == '2':
                        codigo_estacion = input("Ingrese el código de la estación: ")
                        variable = input("Ingrese la variable (ejemplo: temperatura): ")
                        valor = input("Ingrese el valor de la medida: ")
                        try:
                            valor = float(valor)
                            funciones.agregar_medida(codigo_estacion, variable, valor)
                        except ValueError:
                            print("Valor de medida no válido. Debe ser un número.")
                    elif opcion_operador == '3':
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
            
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == '2':  # Usuario visitante
            while True:
                opcion_visitante = menu_visitante()
                if opcion_visitante == '1':
                    print("\n--- Visualización de Estadísticas ---")
                    periodo = seleccionar_periodo()
                    
                    registros = funciones.leer_registros()
                    if periodo == '1':
                        funciones.mostrar_estadisticas(registros, dias=7)
                    elif periodo == '2':
                        funciones.mostrar_estadisticas(registros, dias=30)
                    elif periodo == '3':
                        fecha_inicio = input("Ingrese la fecha de inicio (yyyy-mm-dd): ")
                        fecha_fin = input("Ingrese la fecha de fin (yyyy-mm-dd): ")
                        funciones.mostrar_estadisticas(registros, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
                    else:
                        print("Opción inválida.")
                        
                elif opcion_visitante == '2':
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion == '3':  # Salir del sistema
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa principal
if _name_ == "_main_":
    iniciar_programa()
