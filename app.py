import csv

def llegir_csv(arxiu):
    dades = []
    try:
        with open(arxiu, newline='', encoding='utf-8') as fitxer:
            lector = csv.DictReader(fitxer)
            for fila in lector:
                try:
                    fila['Quantitat_Venuda'] = float(fila['Quantitat_Venuda'])
                    fila['Preu_Unitari'] = float(fila['Preu_Unitari'])
                    fila['IVA'] = float(fila['IVA'])
                    fila['Estoc_Disponible'] = int(fila['Estoc_Disponible'])
                    dades.append(fila)
                except ValueError:
                    print("⚠️ Error en una fila: dades incorrectes o mal formatades.")
    except FileNotFoundError:
        print("⚠️ No s'ha trobat l'arxiu CSV.")
    return dades

# Menú creat per Derek
def mostrar_menu():
    print("\nMenú Principal (creat per Derek)")
    print("1. Calcular facturació del mes (Derek)")
    print("2. Mostrar estoc disponible (Geovany)")
    print("3. Mostrar TOP 3 productes amb més facturació (IKER)")
    print("4. Sortir")

# Funció creada per Derek
def calcular_facturacio(dades):
    total_sin_iva = 0
    total_con_iva = 0

    for fila in dades:
        subtotal = fila['Quantitat_Venuda'] * fila['Preu_Unitari']
        total_sin_iva += subtotal
        total_con_iva += subtotal * (1 + fila['IVA'] / 100)

    print("\n----- FACTURACIÓ DEL MES ----- (Funció feta per Derek)")
    print(f"Total sense IVA: {total_sin_iva:,.2f} €")
    print(f"Total amb IVA: {total_con_iva:,.2f} €")

# Funció creada per Geovany
def mostrar_estoc_disponible(dades):
    print("\n----- ESTOC DISPONIBLE ----- (Funció feta per Geovany)")
    print(f"{'Producte':<20} {'Categoria':<15} {'Estoc':>10}")
    print("-" * 45)

    for fila in dades:
        try:
            print(f"{fila['Producte']:<20} {fila['Categoria']:<15} {fila['Estoc_Disponible']:>10}")
        except ValueError:
            print("⚠️ Error en una fila: dades incorrectes o mal formatades.")

# Funció creada per IKER
def mostrar_top3_facturacio(dades):
    facturacions = {}

    for fila in dades:
        producte = fila['Producte']
        subtotal = fila['Quantitat_Venuda'] * fila['Preu_Unitari']
        if producte in facturacions:
            facturacions[producte] += subtotal
        else:
            facturacions[producte] = subtotal

    # Ordenar de més a menys facturació
    top3 = sorted(facturacions.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n----- TOP 3 PRODUCTES PER FACTURACIÓ ----- (Funció feta per IKER)")
    for i, (producte, total) in enumerate(top3, 1):
        print(f"{i}. {producte:<20} → {total:,.2f} €")

def gestionar_seleccio(opcio, dades):
    if opcio == "1":
        calcular_facturacio(dades)
    elif opcio == "2":
        mostrar_estoc_disponible(dades)
    elif opcio == "3":
        mostrar_top3_facturacio(dades)
    elif opcio == "4":
        print("Sortint...")
        return False
    else:
        print("Opció no vàlida. Si us plau, tria una opció del menú.")
    return True

def menu_principal():
    dades = llegir_csv("dades_botiga.csv")
    if not dades:
        return  # Sortir si no s'han carregat dades

    continuar = True
    while continuar:
        mostrar_menu()
        opcio = input("\nSelecciona una opció: ")
        continuar = gestionar_seleccio(opcio, dades)

if __name__ == "__main__":
    menu_principal()
