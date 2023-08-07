from lectura_archivo import lectura_archivo

lectura = lectura_archivo()


def cargar_Inventario():
    ruta = input("ingrese la ruta: ")
    print("")
    print("----------------Productos agregados----------------")
    lectura.cargar_inventario_inicial(ruta)

def cargar_Movimeinto():
    ruta = input("ingrese la ruta: ")
    print("")
    print("----------------Productos nuevos o vendidos ----------------")
    lectura.cargar_instruccion_movimiento(ruta)



def menu_principal():

    print("")
    print("---------------------------------------------------")
    print("Practica 1 - Lenguajes formales y de programacion")
    print("---------------------------------------------------")
    print("# Sistema de inventario: ")
    print("1. Cargar Inventario inicial")    
    print("2. Cargar Instrucciones de movimientos")    
    print("3. Crear Informe de invetario") 
    print("4. Salir") 
    print("")

    opciones = int(input("Ingrese una opcion: "))   

    if opciones == 1:
        try:
            cargar_Inventario()
        except:
            print("No se encontro el archivo :(")
        menu_principal()
    elif opciones == 2:
        
        cargar_Movimeinto()

        menu_principal()
    elif opciones == 3:
        print("opcion 3")
        menu_principal()
    elif opciones == 4:
        print("Saliendo del programa, vuelva pronto")
        
    else:
        print("Indique una opcion valida")
        menu_principal()

menu_principal()