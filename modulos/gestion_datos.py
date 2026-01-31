# _____ Muestra listado de naves guardadas en el sistema. #______  2) Editar nave

def mostrar_listado_naves(naves):
    print("\n--- LISTADO DE NAVES REGISTRADAS ---\n")

    for i, nave in enumerate(naves, start=1):
        nombre = nave.get("nombre", "Sin nombre")
        armador = nave.get("armador", "Sin armador")
        print(f"{i}) {nombre} - Armador: {armador}")


# _____ Eligir que nave se quiere editar. #______  2) Editar nave

def seleccionar_nave_para_editar(naves):
    while True:
        try:
            seleccion = int(input("\nIngrese el número de la nave que desea ver: "))
            if 1 <= seleccion <= len(naves):
                return naves[seleccion - 1]
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")


# _____ Editando ficha. #______  2) Editar nave

def editar_ficha_nave(nave):
    print("\n" + "=" * 50)
    print("✏️  EDITAR FICHA TÉCNICA DE LA NAVE")
    print("=" * 50)

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
