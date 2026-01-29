# _____ Este módulo contiene funciones simples para capturar información ingresada por el usuario y crear los registros del sistema GO.


# _____ Mostrar menú principal 

def mostrar_menu():
    print("\n--- Mostrar MENÚ PRINCIPAL: ---")
    print("1 Registrar nave")
    print("2 Ver/Editar nave")
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
            print("Error: Ingrese un entero")



# _____________________________________________________________________

from modulos.validaciones import clasificar_categoria_nave, pedir_float, validar_datos_nave, validar_positivos


# _____ Captura una ficha técnica básica de nave y retorna un diccionario.
def cargar_ficha_nave():
   
    print("\n--- REGISTRAR NAVE (FICHA TÉCNICA) ---")
    
# _____ Características generales
    nombre = input("Nombre de la nave: ").strip()
    distintivo_llamada = str(input("Distintivo de llamada: ")).strip().lower()
    tipo = input("Tipo de nave (Barcaza / Wellboat / etc.): ").strip()
    material_casco = input("Material del casco (Acero/Aluminio/ ): ").strip()
    armador = input("Armador: ").strip()
    puerto_matricula = input("Puerto de matrícula: ").strip()

# _____ Datos numéricos (conversión)
    arqueo_bruto = pedir_float("Arqueo bruto (AB): ")
    arqueo_neto = pedir_float("Arqueo neto (AN): ")
    eslora_total = pedir_float("Eslora total (m): ")
    manga_maxima = pedir_float("Manga máxima (m): ")
    manga_moldeada = pedir_float("Manga moldeada (m): ")
    puntal = pedir_float("Puntal (m): ")

    # _____ Operador de comparación: clasificación según arqueo bruto

# VALIDACIÓN
    if not validar_datos_nave(arqueo_bruto, arqueo_neto, eslora_total, manga_maxima, manga_moldeada):
        return None
    
    if not validar_positivos(arqueo_bruto, arqueo_neto, eslora_total, manga_maxima, manga_moldeada, puntal):
        return None

    categoria = clasificar_categoria_nave(arqueo_bruto)


# _____ Observación opcional
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

