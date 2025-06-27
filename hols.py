def calcular_totales_stats():
    """
    Script para solicitar al usuario los valores de estadísticas de un set de equipo
    y calcular los totales para cada estadística principal.
    """
    # --- Definición de las estructuras de datos ---
    variables_principales = ['LBC', 'LBP', 'TAC', 'TAP', 'PUC', 'PUP']
    objetos_equipo = [
        'WEAPON', 'HEAD', 'GLOVES', 'FACE', 'COMP', 'RING', 'TOP', 'BOTTOM',
        'EARRING', 'NECK', 'SHOES', 'TALISMAN', 'BACK', 'EXTRA'
    ]
    slots = ['S1', 'S2', 'S3']

    # Diccionario para almacenar la suma total de cada variable principal
    totales = {variable: 0 for variable in variables_principales}

    print("--- INICIO DE INGRESO DE DATOS ---")
    print("Para cada slot, ingresa el tipo de variable y su valor.")
    print("Si un slot está vacío, solo presiona Enter para omitirlo.\n")

    # --- Bucle para el ingreso de datos ---
    for objeto in objetos_equipo:
        print(f"--- Objeto: {objeto} ---")
        for slot in slots:
            # Bucle para asegurar que la variable ingresada sea válida
            while True:
                variable_ingresada = input(
                    f"  > Slot {slot} - Tipo de variable ({', '.join(variables_principales)}): ").upper()

                if not variable_ingresada:
                    # El usuario presionó Enter, el slot está vacío
                    break

                if variable_ingresada in variables_principales:
                    # La variable es válida, salimos del bucle de validación
                    break
                else:
                    print(f"    [Error] Variable '{variable_ingresada}' no es válida. Intenta de nuevo.")

            # Si se ingresó una variable, solicitar su valor
            if variable_ingresada:
                # Bucle para asegurar que el valor sea un número
                while True:
                    try:
                        valor_ingresado = float(input(f"    > Slot {slot} - Valor de {variable_ingresada}: "))
                        # Sumar el valor al total correspondiente
                        totales[variable_ingresada] += valor_ingresado
                        break
                    except ValueError:
                        print("    [Error] Por favor, ingresa solo un valor numérico.")
        print("-" * (len(objeto) + 14) + "\n")  # Línea separadora

    # --- Muestra de resultados finales ---
    print("\n===================================")
    print("--- TOTALES FINALES ---")
    print("===================================")

    for variable, total in totales.items():
        # Se formatea el total para mostrarlo de forma clara
        print(f"{variable}: {total:g}")  # :g elimina ceros decimales innecesarios

    print("\n--- CÁLCULO COMPLETADO ---")


# --- Ejecutar la función principal ---
if __name__ == "__main__":
    calcular_totales_stats()
