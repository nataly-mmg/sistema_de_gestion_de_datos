# _____ Sistema de Gestión de Datos - Grupo Océanos (GO)

# _____ Descripción:
# _____ Este programa es el punto de entrada del sistema GO, creado para apoyar la gestión
# _____ de naves y proyectos en una oficina de ingeniería naval.
# _____ Autor: Nataly Martínez G.


# _____ Mensaje de bienvenida.
print("\nBienvenido al Sistema de Gestión de Datos de Grupo Océanos.")
print("Esta herramienta ha sido diseñada para apoyar la gestión interna")
print("de naves y proyectos de ingeniería.\n")


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

print("\n--- INICIO DE SESIÓN ---")

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
        print(f"\n--- ACCESO AUTORIZADO. Usuario activo: {usuario_activo} --- \n")

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
from modulos.datos_basicos import cargar_ficha_nave             #______  1) Registrar nave
from modulos.datos_basicos import mostrar_ficha_nave            #______  3) Ver nave
from modulos.gestion_datos import mostrar_listado_naves         #______  2) Editar nave #______  3) Ver nave
from modulos.gestion_datos import seleccionar_nave_para_editar  #______  2) Editar nave #______  3) Ver nave
from modulos.gestion_datos import editar_ficha_nave             #______  2) Editar nave

naves = []
proyectos = []


while True:
    mostrar_menu()     
    opcion = input("\n--- Selecciona una opción: ").strip()

#______ Validación simple de opción 
    if opcion not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        print("\n❌ Opción inválida. Intente nuevamente.\n")
        continue  # vuelve al menú sin ejecutar nada más

#______ 0) Salir
    if opcion == "0":
        print("\nSaliendo del sistema. Gracias por usar GO.\n")
        break  # sale del while True

#______  1) Registrar nave
    if opcion == "1":
        ficha = cargar_ficha_nave()
        if ficha is not None:
            naves.append(ficha)
            print(f"\n--- Nave registrada correctamente. ---")
            print(f"Total naves registradas: {len(naves)}")

#______  2) Editar nave
    elif opcion == "2":
        if not naves:
            print("No hay naves registradas.")
        else:
            mostrar_listado_naves(naves)
            nave = seleccionar_nave_para_editar(naves)
            editar_ficha_nave(nave)

#______  3) Ver nave
    elif opcion == "3":
        if not naves:
            print("No hay naves registradas.")
        else:
            mostrar_listado_naves(naves)
            nave = seleccionar_nave_para_editar(naves)
            mostrar_ficha_nave(ficha)


#______ faltan opciones!...
