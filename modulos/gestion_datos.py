
from modulos.datos_basicos import crear_ficha_nave
from modulos.validaciones import (
    pedir_float_positivo,
    pedir_arqueo_neto_valido,
    pedir_manga_moldeada_valida,
    pedir_manga_maxima_valida,
    clasificar_categoria_nave,  
    )


# _____ Captura una ficha técnica básica de nave y retorna un diccionario. #______  1) Registrar nave
def cargar_ficha_nave(): #______  1) Registrar nave
   
    print("\n" + "~" * 50)
    print("📋 REGISTRAR NAVE (FICHA TÉCNICA)")
    print("~" * 50)

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

    return crear_ficha_nave(
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
        observaciones
    )



# _____ Muestra listado de naves guardadas en el sistema. #______  2) Editar nave

def mostrar_listado_naves(naves):
    print("\n" + "~" * 50)
    print("\n LISTADO DE NAVES REGISTRADAS: \n")
    print("~" * 50)

    for i, nave in enumerate(naves, start=1):
        nombre = nave.get("nombre", "Sin nombre")
        armador = nave.get("armador", "Sin armador")
        print(f"{i}) {nombre} - Armador: {armador}")
        print("~" * 50 + "\n")


# _____ Eligir que nave se quiere editar. #______  2) Editar nave

def seleccionar_nave_para_editar(naves):
    while True:
        try:
            seleccion = int(input("\n Ingrese el número de la nave que desea ver: "))
            if 1 <= seleccion <= len(naves):
                return naves[seleccion - 1]
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")


# _____ Editando ficha. #______  2) Editar nave

def editar_ficha_nave(nave):
    print("\n" + "~" * 50)
    print("✏️  EDITAR FICHA TÉCNICA DE LA NAVE")
    print("~" * 50)

    for clave, valor in nave.items():
        if clave == "historial":
            continue

        etiqueta = clave.replace("_", " ").capitalize()
        print(f"\n{etiqueta} (actual: {valor})")

        nuevo_valor = input("Nuevo valor (ENTER para mantener): ").strip()

        if nuevo_valor != "":

            if isinstance(valor, float):
                try:
                    nuevo_valor = float(nuevo_valor)
                except ValueError:
                    print("❌ Valor inválido, se mantiene el anterior.")
                    continue

            nave[clave] = nuevo_valor

    print("\n✅ Ficha actualizada correctamente.\n")


# ________________________________________________-

from modulos.datos_basicos import trabajos_disponibles
from modulos.datos_basicos import mostrar_trabajos_disponibles
from modulos.validaciones import pedir_trabajos_validos





# _____ Proyectos. #______  seleccionar trabajos 📐 #______  4) Crear proyecto 📐

# _____ Permite seleccionar uno o más trabajos ingresando números separados por coma.
# _____ Retorna una lista de trabajos seleccionados 


def seleccionar_trabajos():
     
     while True:
        trabajos_seleccionados = []

        print("\n📐 SELECCIÓN DE TRABAJOS DEL PROYECTO")
        print("Ingrese los números separados por coma (ej: 1 o 1,3,6)\n")

        for numero, trabajo in trabajos_disponibles.items():
            print(f"{numero}) {trabajo}")

        seleccion = input("\nSelección: ").strip()

        if not seleccion:
            print("❌ Debe ingresar al menos una opción.")
            continue

        partes = seleccion.split(",")

        for item in partes:
            item = item.strip()

            if not item.isdigit():
                continue

            num = int(item)

            if num not in trabajos_disponibles:
                continue

            # Opción OTRO
            if num == 9:
                otro = input("Describa el trabajo: ").strip()
                if otro:
                    trabajos_seleccionados.append(otro)
            else:
                trabajo = trabajos_disponibles[num]
                if trabajo not in trabajos_seleccionados:
                    trabajos_seleccionados.append(trabajo)

        if trabajos_seleccionados:
            return trabajos_seleccionados

        print("❌ No se seleccionaron trabajos válidos. Intente nuevamente.")



# _____ Crear Proyectos.
def cargar_proyecto(numero_proyecto, naves, usuario_activo):

    print("\n📋 CREAR PROYECTO: ")
    print("~" * 50)

    #  Mostrar listado de naves
    print("\n~~~ LISTADO DE NAVES REGISTRADAS:")
    print("~" * 50)

    for i, nave in enumerate(naves, start=1):
        print(f"{i}) {nave['nombre']} - Armador: {nave['armador']}")

    print("~" * 50)

    #  Seleccionar nave por número
    while True:
        try:
            opcion = int(input("Seleccione el número de la nave a la cual cargará el proyecto: "))
            if 1 <= opcion <= len(naves):
                nave_seleccionada = naves[opcion - 1]
                break
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")

    #  Datos del proyecto
    descripcion = input("Descripción general del proyecto: ").strip()

    trabajos = seleccionar_trabajos()

    proyecto = {
        "numero_proyecto": numero_proyecto,
        "nave": nave_seleccionada["nombre"],
        "descripcion": descripcion,
        "trabajos": trabajos,
        "estado": "EN_ESPERA"
    }

    # Registrar en historial de la nave (sin cambiar estructura)
    evento = {
        "fecha": "HOY",  
        "usuario": usuario_activo,
        "accion": "CREAR_PROYECTO",
        "detalle": f"Proyecto N°{numero_proyecto}: {descripcion}"
    }

    nave_seleccionada["historial"].append(evento)

    return proyecto


# _____ Listado de proyectos.

def mostrar_listado_proyectos(proyectos):

    print("\n~~~ 📐 LISTADO DE PROYECTOS REGISTRADOS")
    print("~" * 50)

    for i, p in enumerate(proyectos, start=1):
        print(
            f"{i}) Proyecto N°{p['numero_proyecto']} - "
            f"Nave: {p['nave']} - Estado: {p['estado']}"
        )

    print("~" * 50)



# _____ Seleccione un proyecto.

def seleccionar_proyecto(proyectos, indice):
    return proyectos[indice]

def obtener_proyecto_por_indice(proyectos, indice):
    return proyectos[indice]



def seleccionar_proyecto_para_editar(proyectos):
    while True:
        try:
            seleccion = int(input("\n Ingrese el número del proyecto que desea ver: "))
            if 1 <= seleccion <= len(proyectos):
                return proyectos[seleccion - 1]
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")


# _____ Edita un proyecto.

def editar_proyecto(proyectos):

    if not proyectos:
        print("❌ No hay proyectos registrados.")
        return

    mostrar_listado_proyectos(proyectos)

    try:
        opcion = int(input("Seleccione el número del proyecto a editar: "))
        if opcion < 1 or opcion > len(proyectos):
            print("❌ Número fuera de rango.")
            return
    except ValueError:
        print("❌ Debe ingresar un número válido.")
        return

    proyecto = seleccionar_proyecto(proyectos, opcion - 1)

    print("\n1) Cambiar descripción")
    print("2) Cambiar trabajos asignados")

    op = input("Opción: ").strip()

    if op == "1":
        nueva_desc = input("Nueva descripción: ").strip()
        proyecto["descripcion"] = nueva_desc
        print("✅ Descripción actualizada.")

    elif op == "2":
        nuevos_trabajos = seleccionar_trabajos()
        proyecto["trabajos"] = nuevos_trabajos
        print("✅ Trabajos actualizados.")

    else:
        print("❌ Opción inválida.")



# _____ Cambiar trabajos disponibles en un proyecto.

def cambiar_trabajos_proyecto(proyecto):

    print("\n~~~ 📐 TRABAJOS DISPONIBLES")
    mostrar_trabajos_disponibles()

    trabajos = pedir_trabajos_validos()
    proyecto["trabajos"] = trabajos

    print("✅ Trabajos del proyecto actualizados.")



from modulos.datos_basicos import RESPONSABLES
from modulos.datos_basicos import ESTADOS_PROYECTOS

# _____ Asignar responsable en un proyecto.


def asignar_responsable(proyectos):
    proyecto = seleccionar_proyecto_interactivo(proyectos)
    if proyecto is None:
        return

    print("\n👷 ASIGNAR RESPONSABLE")
    print("~" * 50)

    for i, r in enumerate(RESPONSABLES, start=1):
        print(f"{i}) {r}")

    while True:
        try:
            seleccion = int(input("Seleccione responsable: "))
            if 1 <= seleccion <= len(RESPONSABLES):
                proyecto["responsable"] = RESPONSABLES[seleccion - 1]
                print("✅ Responsable asignado correctamente.")
                return
            print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")


def seleccionar_proyecto_interactivo(proyectos):
    if not proyectos:
        print("❌ No hay proyectos registrados.")
        return None

    print("\n📋 LISTADO DE PROYECTOS")
    print("~" * 50)

    for i, p in enumerate(proyectos, start=1):
        print(f"{i}) Proyecto N°{p['numero_proyecto']} - Nave: {p['nave']} - Estado: {p['estado']}")

    print("~" * 50)

    while True:
        try:
            opcion = int(input("Seleccione el número del proyecto (0 para volver): "))
            if opcion == 0:
                return None
            if 1 <= opcion <= len(proyectos):
                return proyectos[opcion - 1]
            print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")




# _____ Cambiar estado de proyecto

def cambiar_estado_proyecto(proyectos):
    proyecto = seleccionar_proyecto_interactivo(proyectos)
    if proyecto is None:
        return

    print("\n📐 CAMBIAR ESTADO DEL PROYECTO")
    print("~" * 50)

    for i, estado in enumerate(ESTADOS_PROYECTOS, start=1):
        print(f"{i}) {estado}")

    while True:
        try:
            seleccion = int(input("Seleccione nuevo estado: "))
            if 1 <= seleccion <= len(ESTADOS_PROYECTOS):
                proyecto["estado"] = ESTADOS_PROYECTOS[seleccion - 1]
                print("✅ Estado actualizado correctamente.")
                return
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")




# _____ Estadisticas

def mostrar_estadisticas(proyectos):

    print("\n📊 ESTADÍSTICAS DE PROYECTOS")
    print("~" * 40)

    for estado in ESTADOS_PROYECTOS:
        contador = 0
        for p in proyectos:
            if p["estado"] == estado:
                contador += 1

        print(f"{estado}: {contador}")


def eliminar_proyecto(proyectos):
    proyecto = seleccionar_proyecto_interactivo(proyectos)
    if proyecto:
        proyectos.remove(proyecto)
        print("🗑️ Proyecto eliminado correctamente.")
