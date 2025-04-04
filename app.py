def mostrar_menu():
    print("\nMenú Principal")
    print("1. Calcula la facturació del mes")
    print("2. Calcula l'estoc disponible")
    print("3. Resum dels 3 productes mes facturats")
    print("4. Sortir")

def gestionar_seleccio(opcio):
    if opcio == "1":
        print("Has seleccionat Opció 1")
    elif opcio == "2":
        print("Has seleccionat Opció 2")
    elif opcio == "3":
        print("Has seleccionat Opció 3")
    elif opcio == "4":
        print("Sortint...")
        return False
    else:
        print("Opció no vàlida. Si us plau, tria una opció del menú.")
    return True

def menu_principal():
    mostrar_menu()
    continuar = True
    while continuar:
        opcio = input("\nSelecciona una opció: ")
        if opcio == "4":
            print("Sortint...")
            break
        gestionar_seleccio(opcio)

if __name__ == "__main__":
    menu_principal()

# Derek