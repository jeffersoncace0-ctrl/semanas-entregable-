def agregar_producto(inventario, nombre, precio, cantidad): 
    # Validacion para evita nombres con espacios para asegurar consistencia en búsquedas.
    if " " in nombre:
        print("Error: el nombre no puede contener espacios.")
        return False

    # Control para verificar si el producto ya existe en el inventario.
    existente = buscar_producto(inventario, nombre)
    
    if existente:
        print("Error: el producto ya existe.")
        return False

    # Crea un diccionario para el nuevo producto con tipos correctos.
    producto = {
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }

    # Añade el producto a la lista del inventario.
    inventario.append(producto)
    return True


def buscar_producto(inventario, nombre):
    
    # Recorre el inventario para encontrar un producto por su nombre.
    for p in inventario:
        # Compara nombres sin importar mayúsculas o minúsculas.
        if p["nombre"].lower() == nombre.lower():
            return p  # Retorna el producto encontrado.

    return None


def eliminar_producto(inventario, nombre):

    # Busca el producto para eliminarlo del inventario.
    producto = buscar_producto(inventario, nombre)
    
    if producto:
        # Elimina el producto del inventario.
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):

    # Evita cálculos si el inventario está vacío.
    if not inventario:
        return None

    # Calcula el subtotal (precio * cantidad) de un producto.
    def subtotal(p):
        return p["precio"] * p["cantidad"]


    # Calcula el total de unidades y el valor total del inventario.
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)


    # Funciones auxiliares para obtener precio y cantidad de un producto.
    def obtener_precio(p):
        return p["precio"]

    def obtener_cantidad(p):
        return p["cantidad"]


    # Encuentra el producto más caro y el que tiene mayor cantidad en stock.
    mas_caro = max(inventario, key = obtener_precio)
    mayor_stock = max(inventario, key = obtener_cantidad)


    # Devuelve un diccionario con las estadísticas calculadas.
    return {
        "unidades": unidades_totales,
        "valor": valor_total,
        "caro": mas_caro,
        "stock": mayor_stock
    }