import csv

def mostrar_menu():
    print("\nMenú Principal")
    print("1. Calcular facturació del mes")
    print("2. Mostrar estoc disponible")
    print("3. Opció 3")
    print("4. Sortir")

def calcular_facturacio(archivo_csv):
    total_sin_iva = 0
    total_con_iva = 0

    try:
        with open(archivo_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    quantitat = float(fila['Quantitat_Venuda'])
                    preu_unitari = float(fila['Preu_Unitari'])
                    iva = float(fila['IVA'])

                    subtotal = quantitat * preu_unitari
                    total_sin_iva += subtotal
                    total_con_iva += subtotal * (1 + iva / 100)
                except ValueError:
                    print("⚠️ Error en una fila: dades incorrectes o mal formatades.")

        print("\n----- FACTURACIÓ DEL MES -----")
        print(f"Total sense IVA: {total_sin_iva:,.2f} €")
        print(f"Total amb IVA: {total_con_iva:,.2f} €")

    except FileNotFoundError:
        print("⚠️ No s'ha trobat l'arxiu CSV.")

def mostrar_estoc_disponible(archivo_csv):
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            print("\n----- ESTOC DISPONIBLE -----")
            print(f"{'Producte':<20} {'Categoria':<15} {'Estoc':>10}")
            print("-" * 45)

            for fila in lector:
                try:
                    producte = fila['Producte']
                    categoria = fila['Categoria']
                    estoc = int(fila['Estoc_Disponible'])
                    print(f"{producte:<20} {categoria:<15} {estoc:>10}")
                except ValueError:
                    print("⚠️ Error en una fila: dades incorrectes o mal formatades.")
    except FileNotFoundError:
        print("⚠️ No s'ha trobat l'arxiu CSV.")

def gestionar_seleccio(opcio):
    if opcio == "1":
        calcular_facturacio("dades_botiga.csv")
    elif opcio == "2":
        mostrar_estoc_disponible("dades_botiga.csv")
    elif opcio == "3":
        print("Has seleccionat Opció 3")
    elif opcio == "4":
        print("Sortint...")
        return False
    else:
        print("Opció no vàlida. Si us plau, tria una opció del menú.")
    return True

def menu_principal():
    continuar = True
    while continuar:
        mostrar_menu()
        opcio = input("\nSelecciona una opció: ")
        continuar = gestionar_seleccio(opcio)

if __name__ == "__main__":
    menu_principal()
1