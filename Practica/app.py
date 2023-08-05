

def menu_principal():

    print("")
    print("---------------------------------------------------")
    print("Practica 1 - Lenguajes formales y de programacion")
    print("---------------------------------------------------")
    print("# Sistema de inventario: ")
    print("1. Cargar Inventario inicial")    
    print("2. Cargar Instrucciones de movimientos")    
    print("3. Crear Informe de invetario") 
    print("4. Vender producto")
    print("5. Salir") 
    print("")
    opciones = int(input("Ingrese una opcion: "))    
    if opciones == 1:
        print("opcion 1")
        menu_principal()
    elif opciones == 2:
        print("opcion 2")
        menu_principal()
    elif opciones == 3:
        print("opcion 4")
        menu_principal()
    elif opciones == 4:
        print("opcion 4")
        menu_principal()
    elif opciones == 5:
        print("Saliendo del programa, vuelva pronto")
        
    else:
        print("Indique una opcion valida")
        menu_principal()

menu_principal()