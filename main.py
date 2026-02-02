# _____ Sistema de Gestión de Datos - Grupo Océanos (GO)

# _____ Descripción:
# _____ Este programa es el punto de entrada del sistema GO, creado para apoyar la gestión
# _____ de naves y proyectos en una oficina de ingeniería naval.
# _____ Autor: Nataly Martínez G.


# _____ Mensaje de bienvenida.
print("\n" + "~" * 70)
print("\nBienvenido al Sistema de Gestión de Datos de Grupo Océanos.")
print("Esta herramienta ha sido diseñada para apoyar la gestión interna")
print("de naves y proyectos de ingeniería.\n")
print("~" * 70)

# _____ Login usuarios
# _____ Datos de usuario previamente guardados 
usuario1_guardado = "nataly"
contrasena1_guardada = "1234"

usuario2_guardado = "christopher"
contrasena2_guardada = "1234"

usuario3_guardado = "anthony"
contrasena3_guardada = "1234"

# _____ Datos de usuario para realizar pruebas (mas corto y rápido)
usuario4_guardado = "0"
contrasena4_guardada = "0"

# _____ Capturar datos del usuario
# _____ Con strip() para eliminar espacios en blanco y con .lower() para convertir todo en minúscula.

usuario_activo = ""
intentos = 3

# _____ Comparación de datos

while usuario_activo == "" and intentos > 0:
    usuario_ingresado = input("Ingresa tu nombre de usuario: ").strip().lower()
    contrasena_ingresada = input("Ingresa tu contraseña: ").strip()

    if (usuario_ingresado == usuario1_guardado and contrasena_ingresada == contrasena1_guardada) \
        or (usuario_ingresado == usuario2_guardado and contrasena_ingresada == contrasena2_guardada) \
        or (usuario_ingresado == usuario3_guardado and contrasena_ingresada == contrasena3_guardada) \
        or (usuario_ingresado == usuario4_guardado and contrasena_ingresada == contrasena4_guardada):

        usuario_activo = usuario_ingresado
        print(f"\n~~~ ACCESO AUTORIZADO. Usuario activo: {usuario_activo}.\n")

    else:
        intentos -= 1
        print("\nCredenciales inválidas. Acceso denegado.")
        print(f"Intentos restantes: {intentos}\n")

if usuario_activo == "":
    print("Se superó el número máximo de intentos. El sistema se cerrará.")
    exit()



# __________________________________________________________________________________ 

# _____ MENU GENERAL

from modulos.datos_basicos import mostrar_menu
from modulos.datos_basicos import mostrar_ficha_nave            #______  3) Ver nave
from modulos.datos_basicos import mostrar_ficha_proyecto        #______  6) Ver proyectos 📐


from modulos.gestion_datos import cargar_ficha_nave             #______  1) Registrar nave
from modulos.gestion_datos import mostrar_listado_naves         #______  2) Editar nave #______  3) Ver nave
from modulos.gestion_datos import seleccionar_nave_para_editar  #______  2) Editar nave #______  3) Ver nave
from modulos.gestion_datos import editar_ficha_nave             #______  2) Editar nave

from modulos.gestion_datos import cargar_proyecto               #______  4 Crear proyecto 📐
from modulos.gestion_datos import mostrar_listado_proyectos     #______  6 Ver proyectos 📐
from modulos.gestion_datos import editar_proyecto               #______  5 Editar proyecto 📐


# from modulos.gestion_datos import seleccionar_proyecto_para_editar
# from modulos.validaciones import pedir_numero_en_rango
# from modulos.validaciones import pedir_trabajos_validos



naves = []
proyectos = []
numero_proyecto = 1

while True:
    mostrar_menu()     
    opcion = input("\n~~ Selecciona una opción: ").strip()
    print("~" * 50)



#______ Validación simple de opción 
    if opcion not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        print("\n❌ Opción inválida. Intente nuevamente.\n")
        continue  # vuelve al menú sin ejecutar nada más

#______ 0) Salir
    if opcion == "0":
        print("\nSaliendo del sistema. Gracias por usar GO.\n")
        break  # sale del while True

#______  1 Registrar nave 🚢
    if opcion == "1":
        ficha = cargar_ficha_nave()
        if ficha is not None:
            naves.append(ficha)
            print(f"\n~~~ Nave registrada correctamente. ~~~")
            print(f"Total naves registradas: {len(naves)}")

#______  2 Editar nave 🚢
    elif opcion == "2":
        if not naves:
            print("No hay naves registradas.")
        else:
            mostrar_listado_naves(naves)
            nave = seleccionar_nave_para_editar(naves)
            editar_ficha_nave(nave)

#______  3 Ver nave 🚢
    elif opcion == "3":
        if not naves:
            print("No hay naves registradas.")
        else:
            mostrar_listado_naves(naves)
            nave = seleccionar_nave_para_editar(naves)
            mostrar_ficha_nave(ficha)

#______  4 Crear proyecto 📐
    elif opcion == "4":
        if not naves:
            print("❌ No hay naves registradas. Debe registrar una nave primero.")
            continue

        proyecto = cargar_proyecto(numero_proyecto, naves, usuario_activo)

        if proyecto:
            proyectos.append(proyecto)
            print(f"\n~~~ Proyecto N° {numero_proyecto} creado correctamente.\n")
            numero_proyecto += 1

#______  5 Editar proyecto 📐

    elif opcion == "5":  
        editar_proyecto(proyectos)



#______  6 Ver proyectos 📐
 
    elif opcion == "6":

        if not proyectos:
            print("❌ No hay proyectos registrados.")
            continue

        mostrar_listado_proyectos(proyectos)

        try:
            seleccion = int(input("Ingrese el número del proyecto que desea ver (0 para volver): "))

            if seleccion == 0:
                continue

            if 1 <= seleccion <= len(proyectos):
                proyecto = proyectos[seleccion - 1]
                mostrar_ficha_proyecto(proyecto)
            else:
                print("❌ Número fuera de rango.")

        except ValueError:
            print("❌ Debe ingresar un número válido.")






















#______ faltan opciones!...
