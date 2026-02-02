# _____ Este módulo contiene la estructura para capturar información ingresada por el usuario y crear los registros del sistema GO.


# _____ Mostrar menú principal 

def mostrar_menu():
    print("\n" + "~" * 50)
    print("\n Mostrar MENÚ PRINCIPAL: ")
    print("~" * 50)
    print("1 Registrar nave 🚢")
    print("2 Editar nave 🚢")
    print("3 Ver nave 🚢")
    print("4 Crear proyecto 📐")
    print("5 Editar proyecto 📐")
    print("6 Ver proyectos 📐")
    print("7 Asignar responsable 👷")
    print("8 Cambiar estado de proyecto 📐")
    print("9 Estadísticas 📊")
    print("10 Ver historial por nave 🗂️")
    print("0 Salir")
    print("~" * 50 + "\n")


# _________________________________ #______  1) Registrar nave __ ficha


def crear_ficha_nave(
    nombre,
    distintivo_llamada,
    tipo,
    categoria,
    material_casco,
    armador,
    puerto_matricula,
    arqueo_bruto,
    arqueo_neto,
    eslora_total,
    manga_maxima,
    manga_moldeada,
    puntal,
    observaciones=""
):
    return {
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


# _________________________________ # _____ Mostrar ficha ___ 3 Ver nave 🚢

def mostrar_ficha_nave(ficha: dict):
    print("\n" + "~" * 50)
    print("📋 FICHA TÉCNICA DE LA NAVE")
    print("~" * 50)

    for clave, valor in ficha.items():
        if clave == "historial":
            continue  

        etiqueta = clave.replace("_", " ").capitalize()
        print(f"{etiqueta:<25}: {valor}")




# ________________________________________________-


# _____ Proyectos. #______  seleccionar trabajos 📐 #______  4) 5) Crear/editar proyecto 📐

trabajos_disponibles = {
    1: "Plano de Arreglo General",
    2: "Plano de Seguridad",
    3: "Plano de Líneas",
    4: "Plano de Combustible",
    5: "Plano de Achique y Lastre",
    6: "Estudio de Estabilidad",
    7: "Manual de Sujeción de Carga",
    8: "Memoria de Cálculo de Arqueo",
    9: "Otro (especificar)"
}

estados_proyectos = ["Creado", "En ejecución", "Finalizado", "Suspendido"]


def mostrar_trabajos_disponibles():
    for i, t in enumerate(trabajos_disponibles, start=1):
        print(f"{i}) {t}")




# _________________________________ # _____ Mostrar ficha proyecto ___ 6 Ver proyectos 📐

def mostrar_ficha_proyecto(proyecto):
    print("\n" + "~" * 50)
    print("\n📋 FICHA DEL PROYECTO")
    print("~" * 50)

    print(f"N° Proyecto : {proyecto['numero_proyecto']}")
    print(f"Nave        : {proyecto['nave']}")
    print(f"Descripción : {proyecto['descripcion']}")
    print(f"Estado      : {proyecto['estado']}")

    print("\nTrabajos:")
    for t in proyecto["trabajos"]:
        print(f" - {t}")

    print("~" * 50)

