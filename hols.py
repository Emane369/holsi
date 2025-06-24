# Accesorios y slots
slots = ["S1", "S2", "S3"]
accesorios = [
    "Weapon", "Head", "Face", "Gloves", "Ring", "Earring", "Talisman",
    "Top", "Neck", "Back", "Comp", "Bottoms", "Shoes", "Extra"
]

# Estructura para almacenar datos
data = {
    slot: {} for slot in slots
}
extras = {}

# Función para ingresar valores
def pedir_valores():
    print("\n--- Ingreso de valores por slot ---\n")
    for slot in slots:
        print(f"\n--- {slot} ---")
        for acc in accesorios:
            while True:
                try:
                    valor = int(input(f"Ingrese valor para {acc} en {slot}: "))
                    break
                except ValueError:
                    print("Por favor, ingresa un número entero.")
            data[slot][acc] = valor

    print("\n--- Ingreso de extras ---")
    for extra in ["Tarots", "SS"]:
        while True:
            try:
                valor = int(input(f"Ingrese valor para {extra}: "))
                break
            except ValueError:
                print("Por favor, ingresa un número entero.")
        extras[extra] = valor

# Función para calcular totales
def calcular_totales():
    total_por_slot = {slot: sum(data[slot].values()) for slot in slots}
    total_general = sum(total_por_slot.values()) + sum(extras.values())

    return {
        "LBP": total_por_slot["S1"],
        "LBC": total_por_slot["S2"],
        "TAC": total_por_slot["S3"],
        "TAP": extras["Tarots"],
        "PUP": extras["SS"],
        "PUC": total_general
    }

# Ejecutar el ingreso de datos y mostrar resultados
if __name__ == "__main__":
    pedir_valores()
    print("\n--- Resultados ---")
    totales = calcular_totales()
    for clave, valor in totales.items():
        print(f"{clave}: {valor}")
