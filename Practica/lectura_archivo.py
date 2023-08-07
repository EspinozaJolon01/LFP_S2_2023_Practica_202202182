class lectura_archivo:

    def __init__(self) :
        self.producto = [] 
        self.cantidad = []
        self.precios = []
        self.ubicacion = []
        #lista
        self.lista = []
        self.listas_nuevo_produc = []
        #lista para nuevo producto 
        self.nuevo_producto = []
        self.nueva_cantaidad = []
        self.nueva_ubicaciones = []
        #guarda el indice 0
        self.verificar = []
    

    def cargar_inventario_inicial(self,ruta):
        self.lista = [] 

        archivo  = open(f"C:/Users/Usuario/Desktop/Usac/13-Semestre4/LenguajesFormales/Lab-Lenguajes/Practica 1/Practica/{ruta}.inv","r")

        list = archivo.readline()
        while list:
            self.lista.append(list)
            list = archivo.readline()
        
        archivo.close

        for productos in self.lista:
            articulo = productos.split(" ",1)
            articulo.pop(0)
            self.producto.append(articulo[0].split(";")[0])
            self.cantidad.append(articulo[0].split(";")[1])
            self.precios.append(articulo[0].split(";")[2])
            self.ubicacion.append(articulo[0].split(";")[3])


        print(self.producto)
        print(self.cantidad)
        print(self.precios)
        print(self.ubicacion)


        return self.producto,self.cantidad,self.precios,self.ubicacion
    
    

    def cargar_instruccion_movimiento(self,ruta):
        

        archivo  = open(f"C:/Users/Usuario/Desktop/Usac/13-Semestre4/LenguajesFormales/Lab-Lenguajes/Practica 1/Practica/{ruta}.mov","r")

        list = archivo.readline()
        while list:
            self.listas_nuevo_produc.append(list)
            list = archivo.readline()
        
        archivo.close

        for nuevo_produc in self.listas_nuevo_produc:
            articulo = nuevo_produc.split(" ",1)
            
            self.verificar.append(articulo[0])
            
            articulo.pop(0)
            self.nuevo_producto.append(articulo[0].split(";")[0])
            self.nueva_cantaidad.append(articulo[0].split(";")[1])
            self.nueva_ubicaciones.append(articulo[0].split(";")[2])
        
        for i, verificacion in enumerate(self.verificar):
            self.verificar_producto(verificacion,self.nuevo_producto[i],self.nueva_cantaidad[i],self.nueva_ubicaciones[i])
            #self.nuevo_producto[i],self.nueva_cantaidad[i],self.nueva_ubicaciones[i]

        return self.listas_nuevo_produc

    def verificar_producto(self,verificar,producto,cantidad,ubicacion):
        if verificar == "agregar_stock":
            self.registar_bodega(producto,cantidad,ubicacion)
            
        elif verificar == "vender_producto":
            self.vender_prodcuto(producto,cantidad,ubicacion)

        else:
            print("Opción inválida")

    def registar_bodega(self,produc,cantidad,ubicaciones):
        
        for indice, producto_registrado in enumerate(self.producto):
            if producto_registrado == produc and self.ubicacion[indice].strip() == ubicaciones.strip():
                self.cantidad[indice] = str(int(self.cantidad[indice]) + int(cantidad))
                print("- Se agregó stock:", produc, ubicaciones, "Cantidad actual:", self.cantidad[indice])
                break
        else:
            print("*Error,articulo no encontrado")
            

    def vender_prodcuto(self,produc,cantidad,ubicaciones):
        found = False
        for i, producto_vender in enumerate(self.producto):
            if producto_vender == produc and self.ubicacion[i].strip() == ubicaciones.strip():
                found = True
                if int(cantidad) <= int(self.cantidad[i]):
                    self.cantidad[i] = str(int(self.cantidad[i]) - int(cantidad))
                    print("-- Se vendio en stock:", produc, ubicaciones, "Cantidad actual:", self.cantidad[i])
                    break
                else:
                    print("*-Cantidad excede la existente para el artículo:", produc,ubicaciones)
        if not found:
            print("**Error,articulo no encontrado")

    def crear_arhivo_txt(self,ruta):
        pass
