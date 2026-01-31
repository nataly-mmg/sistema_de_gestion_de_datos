
# _____ Reglas y validaciones del sistema GO

    
# _____ Solicita un número positivo. Repite hasta que el usuario ingrese un valor válido. #______  1) Registrar nave

def pedir_float_positivo(mensaje: str) -> float:
  
    while True:
        valor = pedir_float(mensaje)

        if valor > 0:
            return valor
        else:
            print("❌ Error: Debe ingresar un número positivo mayor a 0.")


# _____ Solicita que AN sea menor que AB. #______  1) Registrar nave

def pedir_arqueo_neto_valido(arqueo_bruto: float) -> float:
 
    while True:
        arqueo_neto = pedir_float_positivo("Arqueo neto (AN): ")
        if arqueo_neto < arqueo_bruto:
            return arqueo_neto
        print("❌ Error: El Arqueo Neto debe ser menor que el Arqueo Bruto.")


# _____ Solicita que la manga máxima sea menor que la eslora total. #______  1) Registrar nave

def pedir_manga_maxima_valida(eslora_total: float) -> float:
    
    while True:
        manga_maxima = pedir_float_positivo("Manga máxima (m): ")
        if manga_maxima < eslora_total:
            return manga_maxima
        print("❌ Error: La Manga Máxima debe ser menor que la Eslora Total.")


# _____ Solicita que la manga moldeada sea menor que la manga máxima. #______  1) Registrar nave

def pedir_manga_moldeada_valida(manga_maxima: float) -> float:
    
    while True:
        manga_moldeada = pedir_float_positivo("Manga moldeada (m): ")
        if manga_moldeada < manga_maxima:
            return manga_moldeada
        print("❌ Error: La Manga Moldeada debe ser menor que la Manga Máxima.")


# _____ Clasifica categoria de la nave. #______  1) Registrar nave

def clasificar_categoria_nave(arqueo_bruto):

    if arqueo_bruto > 100:
        return "Mayor"
    else:
        return "Menor"


# _____     Solicita números y no acepta letras. Repite hasta que el usuario ingrese un valor válido. #______  1) Registrar nave

def pedir_float(mensaje):
    
    while True:
        valor = input(mensaje).strip()

        try:
            return float(valor)
        except ValueError:
            print("❌ Error: Debe ingresar solo números.\n")
