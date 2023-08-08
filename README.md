# Manual tecnico

## José Luis Espinoza Jolón - 202202182

Mi proyecto consiste en 2 documentos de python, lectura_archivo donde esta todos las funciones y app es el archivo principal

## app.py

Funcion menu_principal, imprimer todas las opciones que el usuario pueda ingresar

```python
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
        try:
            cargar_Movimeinto()
        except:
            print("No se encontro el archivo :(")
        menu_principal()
    elif opciones == 3:
        cargar_archivo()
        menu_principal()
    elif opciones == 4:
        print("Saliendo del programa, vuelva pronto")
        
    else:
        print("Indique una opcion valida")
        menu_principal()
```
- Opcion 1: esta opcion sirve para que el usuario pueda cargar el inventario inicial 
esta es la funcion, desde la clase lenguaje_archivo
```python
def cargar_Inventario():
    ruta = input("ingrese la ruta: ")
    print("")
    print("----------------Productos agregados----------------")
    lectura.cargar_inventario_inicial(ruta)
```
- Opcion 2: esta opcion sirve para que el usuario pueda cargar el archivo que contiene agregar y vender al stock 
esta es la funcion, desde la clase lenguaje_archivo
```python
def cargar_Movimeinto():
    ruta = input("ingrese la ruta: ")
    print("")
    print("----------------Productos nuevos o vendidos ----------------")
    lectura.cargar_instruccion_movimiento(ruta)
```

- Opcion 3: Esta opcion el usuario puede crear en un archivo txt, el inventario de todos los prodcutos
esta es la funcion, desde la clase lenguaje_archivo
```python
def cargar_archivo():
    print("")
    print("----------------Archivo txt ----------------")
    lectura.crear_arhivo_txt()
```
- Opcion 4: para salir del programa 

importante es llamar a la clase lectura_archivo para poder manejar sus funciones dentro de la clase app
```python
from lectura_archivo import lectura_archivo

lectura = lectura_archivo()
```
## lectura_archivo
En esta clase realizamos las funciones de nuestro proyecto 

1. El constructor de la clase: donde creamos e inicializamos nuestra listas
   
   ```python
    def __init__(self) :
        self.producto = [] 
        self.cantidad = []
        self.precios = []
        self.ubicacion = []
        self.valor_total_prodcuto = []
        #lista
        self.lista = []
        self.listas_nuevo_produc = []
        #lista para nuevo producto 
        self.nuevo_producto = []
        self.nueva_cantaidad = []
        self.nueva_ubicaciones = []
        #guarda el indice 0
        self.verificar = []   
   
   ```
2. Funcion cargar_inventario_inicial, nos pide 2 parametros el self, la ruta, va ser el nombre a buscar para poder abrir nuestro documento
   y convertilo en listas, se realizo la separcion de producto,cantidad, precio y bodega en diferentes listas.
   
```python
       def cargar_inventario_inicial(self,ruta):
        self.lista = [] 

        archivo  = open(f"C:/Users/Usuario/Desktop/documentos/{ruta}.inv","r")

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
```
3. Funcion cargar_instruccion_movimiento, de la misma forma de la funcion cargar_inventario_incial se realizó, solo se realizó un for para poder
   mandar como parametro la verificacion, los productos,cantidad, ubicaciones nuevas para usarlo en otro funcion.

```python
    def cargar_instruccion_movimiento(self,ruta):
        

        archivo  = open(f"C:/Users/Usuario/Desktop/documentos/{ruta}.mov","r")

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
```

4. Funcion verificar_producto, se reliza para comprobacion si es agregar o vender, dentro se llama otra funcion para realizar dicha funcion.
 ```python
    def verificar_producto(self,verificar,producto,cantidad,ubicacion):
        if verificar == "agregar_stock":
            self.registar_bodega(producto,cantidad,ubicacion)
            
        elif verificar == "vender_producto":
            self.vender_prodcuto(producto,cantidad,ubicacion)

        else:
            print("Opción inválida")
 ```
5. Función registar_bodega, consiste en verificar si el nombre que se encuentra en bodiga es el mismo en que ingresa el usuario y de la misma
   manera con bodega se realizara el agregar stock, de lo contrario le mandará un mensaje de error

 ```python
    def registar_bodega(self,produc,cantidad,ubicaciones):
        
        for indice, producto_registrado in enumerate(self.producto):
            if producto_registrado == produc and self.ubicacion[indice].strip() == ubicaciones.strip():
                self.cantidad[indice] = str(int(self.cantidad[indice]) + int(cantidad))
                print("- Se agregó stock:", produc, ubicaciones, "Cantidad actual:", self.cantidad[indice])
                break
        else:
            print("*Error,articulo no encontrado")
 ```
6. Función vender_prodcuto, verificar que sea el mismo nombre y bodega, tambien que la cantidad que quiere el usuario sea menor o igual a la que esta
   en bodega, para poder hacer una venta, si no aparecerá un error.
   
 ```python
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
 ```
7. Funcion crear_arhivo_txt, realiza la creación del archivo txt del inventariado.
```python
    def crear_arhivo_txt(self):
        
        nombre_archivo = "inventario.txt"   
        try:
            with open(nombre_archivo, 'w') as archivo:
                archivo.write("Inventario:\n")
                archivo.write("{:<14} {:<14} {:<14} {:<14} {:<14}\n".format("Producto","Cantidad","Precio","Bodega","Valor total"))
                archivo.write("-" * 70 + "\n")
                for i in range(len(self.producto)):
                    valor_total = int(self.cantidad[i]) * float(self.precios[i])
                    self.valor_total_prodcuto.append(valor_total)
                    archivo.write("{:<14} {:<14} {:<14} {:<20} {:>60.2f}\n".format(str(self.producto[i]), str(self.cantidad[i]), str(self.precios[i]), str(self.ubicacion[i]), self.valor_total_prodcuto[i]))
                
            print("Archivo de inventario creado exitosamente. ")
        
        except Exception as e:
            print("Error al crear el arivho de invetario: ",e)
```
   
