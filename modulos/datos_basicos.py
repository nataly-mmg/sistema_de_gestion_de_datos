# _____ Este módulo contiene funciones simples para capturar información ingresada por el usuario y crear los registros del sistema GO.


# _____ Mostrar menú principal 

def mostrar_menu():
    print("\n--- Mostrar MENÚ PRINCIPAL: ---")
    print("1 Registrar nave")
    print("2 Editar nave")
    print("3 Ver nave")
    print("3 Crear proyecto")
    print("4 Ver/editar proyectos")
    print("5 Asignar responsable")
    print("6 Cambiar estado de proyecto")
    print("7 Estadísticas")
    print("8 Ver historial por nave")
    print("0 Salir")


def leer_int(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print(" ❌ Error: Ingrese un entero")

def mostrar_ficha_nave(ficha: dict):
    print("\n" + "=" * 50)
    print("📋 FICHA TÉCNICA DE LA NAVE")
    print("=" * 50)

    for clave, valor in ficha.items():
        if clave == "historial":
            continue  

        etiqueta = clave.replace("_", " ").capitalize()
        print(f"{etiqueta:<25}: {valor}")

    print("=" * 50 + "\n")


# _____________________________________________________________________ #______  1) Registrar nave

from modulos.validaciones import (
    pedir_float_positivo,
    pedir_arqueo_neto_valido,
    pedir_manga_moldeada_valida,
    pedir_manga_maxima_valida,
    clasificar_categoria_nave,  
    )


# _____ Captura una ficha técnica básica de nave y retorna un diccionario. #______  1) Registrar nave
def cargar_ficha_nave(): #______  1) Registrar nave
   
    print("\n--- REGISTRAR NAVE (FICHA TÉCNICA) ---")
    
# _____ Características generales. #______  1) Registrar nave
    nombre = input("Nombre de la nave: ").strip()
    distintivo_llamada = str(input("Distintivo de llamada: ")).strip().lower()
    tipo = input("Tipo de nave (Barcaza / Wellboat / etc.): ").strip()
    material_casco = input("Material del casco (Acero/Aluminio/ ): ").strip()
    armador = input("Armador: ").strip()
    puerto_matricula = input("Puerto de matrícula: ").strip()

# _____ Datos numéricos (conversión). #______  1) Registrar nave
    arqueo_bruto = pedir_float_positivo("Arqueo bruto (AB): ")
    arqueo_neto = pedir_arqueo_neto_valido(arqueo_bruto)
    eslora_total = pedir_float_positivo("Eslora total (m): ")
    manga_maxima = pedir_manga_maxima_valida(eslora_total)
    manga_moldeada = pedir_manga_moldeada_valida(manga_maxima)
    puntal = pedir_float_positivo("Puntal (m): ")

    categoria = clasificar_categoria_nave(arqueo_bruto)

# _____ Observación opcional. #______  1) Registrar nave
    observaciones = input("Observaciones (opcional): ").strip()


    ficha = {
        "nombre": nombre,
        "distintivo_llamada": distintivo_llamada,
        "tipo": tipo,
        "categoria": categoria,
        "material_casco": material_casco,
        "armador": armador,
        "puerto_matricula": puerto_matricula,
        "arqueo_bruto": arqueo_bruto,
        "arqueo_neto": arqueo_neto,
        "eslora_total_m": eslora_total,
        "manga_maxima_m": manga_maxima,
        "manga_moldeada_m": manga_moldeada,
        "puntal_m": puntal,

        "observaciones": observaciones,
        "historial": []
    }

    return ficha


# ________________________________________________-

