class lectura_archivo:

    def __init__(self) :
        self.producto = [] 
        self.cantidad = []
        self.precios = []
        self.ubicacion = []
        self.lista = []
        #lista para nuevo producto 
        self.nuevo_producto = []
        self.nueva_cantaidad = []
        self.nueva_ubicaciones = []
    

    def cargar_inventario_inicial(self,ruta):
        lista = [] 

        archivo  = open(f"C:/Users/Usuario/Desktop/Usac/13-Semestre4/LenguajesFormales/Lab-Lenguajes/Practica 1/Practica/{ruta}.inv","r")

        list = archivo.readline()
        while list:
            lista.append(list)
            list = archivo.readline()
        
        archivo.close

        for productos in lista:
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
        print(self.producto[0])

        return self.producto,self.cantidad,self.precios,self.ubicacion
    
    
    def cargar_instruccion_movimiento(self,ruta):
        
        archivo  = open(f"C:/Users/Usuario/Desktop/Usac/13-Semestre4/LenguajesFormales/Lab-Lenguajes/Practica 1/Practica/{ruta}.mov","r")

        list = archivo.readline()
        while list:
            self.lista.append(list)
            list = archivo.readline()
        
        archivo.close

        for nuevo_producto in self.lista:
            articulo = nuevo_producto.split(" ",1)
            articulo.pop(0)
            self.nuevo_producto.append(articulo[0].split(";")[0])
            self.nueva_cantaidad.append(articulo[0].split(";")[1])
            self.nueva_ubicaciones.append(articulo[0].split(";")[2])

        for i,indicaciones in enumerate(self.lista):
            self.verificar_producto(indicaciones,self.nuevo_producto[i],self.nueva_cantaidad[i], self.nueva_ubicaciones[i])
        

        print(self.lista)


    def verificar_producto(self,indicaciones,nombre,cantadad,ubcaciones):
        pass
    
            
        
    


    

    
    