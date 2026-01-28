# _____ Este módulo contiene funciones simples para capturar información ingresada por el usuario y crear los registros del sistema GO.

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
    arqueo_bruto = float(input("Arqueo bruto (AB): ").strip())
    arqueo_neto = float(input("Arqueo neto (AN): ").strip())
    eslora_total = float(input("Eslora total (m): ").strip())
    manga_maxima = float(input("Manga máxima (m): ").strip())
    manga_moldeada = float(input("Manga moldeada (m): ").strip())
    puntal = float(input("Puntal (m): ").strip())


# _____ Operador de comparación: clasificación según arqueo bruto
    if arqueo_bruto > 100:
         categoria = "Mayor"
    else:
         categoria = "Menor"



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




