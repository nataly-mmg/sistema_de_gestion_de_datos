
# _____ Reglas y validaciones del sistema GO

    
    
# _____ Validación booleana

def validar_positivos(arqueo_bruto, arqueo_neto, eslora_total, manga_maxima, manga_moldeada, puntal):
    if (arqueo_bruto > 0 and arqueo_neto > 0 and eslora_total > 0 and
        manga_maxima > 0 and manga_moldeada > 0 and puntal > 0):
        return True
    else:
        print("Debe ingresar un valor válido: todos los valores numéricos deben ser positivos.")
        return False



# _____ Valida coherencia de datos dimensionales de la nave.

def validar_datos_nave(arqueo_bruto, arqueo_neto, eslora_total, manga_maxima, manga_moldeada):

    # Operador de comparación: AB debe ser mayor que AN
    if arqueo_bruto <= arqueo_neto:
        print("\nDebe ingresar un valor válido: el Arqueo Bruto debe ser mayor al Arqueo Neto.")
        return False

    # Operador de comparación: eslora mayor que manga máxima
    elif eslora_total <= manga_maxima:
        print("\nDebe ingresar un valor válido: la Eslora Total debe ser mayor a la Manga Máxima.")
        return False

    # Operador de comparación: manga máxima mayor que manga moldeada
    elif manga_maxima <= manga_moldeada:
        print("\nDebe ingresar un valor válido: la Manga Máxima debe ser mayor a la Manga Moldeada.")
        return False

    else:
        print("\nDatos dimensionales válidos.")
        return True




# _____ Clasifica categoria de la nave.

def clasificar_categoria_nave(arqueo_bruto):

    if arqueo_bruto > 100:
        return "Mayor"
    else:
        return "Menor"


# _____     Solicita un número decimal. Repite hasta que el usuario ingrese un valor válido.

def pedir_float(mensaje):
    
    while True:
        valor = input(mensaje).strip()

        try:
            return float(valor)
        except ValueError:
            print("❌ Error: Debe ingresar solo números.\n")
