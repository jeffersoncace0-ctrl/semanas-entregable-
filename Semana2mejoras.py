# Lista donde se almacenan los productos
inventario = []
# Función para agregar productos al inventario
def agregar_producto():
    
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    # Cada producto se guarda como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(producto)
    
    print("Producto agregado correctamente")
    
# Función para mostrar todos los productos
def mostrar_inventario():
    
    # Validar si el inventario está vacío
    if len(inventario) == 0:
        print("El inventario está vacío")
    
    else:
        print("\nInventario de productos:")
        
        # Recorrer inventario con for
        for p in inventario:
            print("Producto:", p["nombre"], 
                "| Precio:", p["precio"], 
                "| Cantidad:", p["cantidad"])
            
# Función para calcular estadísticas del inventario
def calcular_estadisticas():
    
    total_valor = 0
    
    # Calcular precio * cantidad
    for p in inventario:
        total_valor += p["precio"] * p["cantidad"]
    
    print("\nEstadísticas del inventario")
    print("Valor total del inventario:", total_valor)
    print("Cantidad de productos registrados:", len(inventario))
    
# Menú principal del sistema
opcion = 0

while opcion != 4:
    
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    
    opcion = int(input("Ingrese su opcion para continuar: "))
    
    # Validación con condicionales
    if opcion == 1:
        agregar_producto()
    
    elif opcion == 2:
        mostrar_inventario()
    
    elif opcion == 3:
        calcular_estadisticas()
    
    elif opcion == 4:
        print("Saliendo del programa...")
    
    else:
        print("Opción inválida, intente nuevamente")


# Comentario final
# Este programa permite gestionar un inventario básico utilizando listas,
# diccionarios, condicionales y bucles en Python. Permite agregar productos,
# mostrar el inventario y calcular estadísticas como el valor total.