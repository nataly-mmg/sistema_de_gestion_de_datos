# _____ Sistema de Gestión de Datos - Grupo Océanos (GO)

# _____ Descripción:
# _____ Este programa es el punto de entrada del sistema GO, creado para apoyar la gestión
# _____ de naves y proyectos en una oficina de ingeniería naval.
# _____ Autor: Nataly Martínez G.


# _____ Mensaje de bienvenida.
print("\nBienvenido al Sistema de Gestión de Datos de Grupo Océanos.")
print("Esta herramienta ha sido diseñada para apoyar la gestión interna")
print("de naves y proyectos de ingeniería.\n")

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

print("INICIO DE SESIÓN")

# _____ Capturar datos del usuario
# _____ Con strip() para eliminar espacios en blanco y con .lower() para convertir todo en minúscula.

usuario_ingresado = input("Ingresa tu nombre de usuario: ").strip().lower()
contrasena_ingresada = input("Ingresa tu contraseña: ").strip()

usuario_activo = ""

# _____ Comparación de datos
if usuario_ingresado == usuario4_guardado and contrasena_ingresada == contrasena4_guardada:
    usuario_activo = usuario_ingresado
    print(f"\nAcceso autorizado. Usuario activo: {usuario_activo}\n")
