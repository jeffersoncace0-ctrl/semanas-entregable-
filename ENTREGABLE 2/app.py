import servicios 
import archivos
# Lista vacía para almacenar los productos.
inventario = []

def ejecutar_menu():
    global inventario
    
    # Control del menú principal hasta que el usuario elige salir.
    opcion = " "
    while opcion != "9":
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar | 2. Mostrar | 3. Buscar | 4. Actualizar producto | 5. Eliminar | 6. Estadísticas")
        print("7. Guardar CSV | 8. Cargar CSV | 9. Salir")
        
        opcion = input("Seleccione opción: ")
        # Agregar producto: validación de nombre para evitar entradas vacías.
        if opcion == "1":
            nombre = ""
            while not nombre.strip():
                nombre = input("Nombre: ")
                if not nombre.strip():
                    print("Error: el nombre no puede estar vacío.")
            # Validación del precio para que sea un número positivo.
            precio = 0
            while precio <= 0:
                try:
                    precio = float(input("Precio: "))
                    if precio <= 0:
                        print("Error: el precio debe ser mayor a 0")
                except ValueError:
                    print("Error: ingrese un número válido.")
            # Validación para que  solo se permiten números enteros positivos.
            cantidad = 0
            while cantidad <= 0:
                try:
                    entrada = input("Cantidad: ")
                    if "." in entrada:
                        print("Error: la cantidad debe ser un número entero.")
                        continue
                    
                    cantidad = int(entrada)
                    if cantidad <= 0:
                        print("Error: la cantidad debe ser mayor a 0.")
                except ValueError:
                    print("Error: ingrese un número entero válido.")

            # Agrega el producto al inventario.
            servicios.agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto agregado con éxito.")

        elif opcion == "2":
            # Muestrar los productos en el inventario.
            if not inventario:
                print("El inventario está vacío.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for p in inventario:
                    print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

        elif opcion == "3":
            nombre_busqueda = input("Ingrese el nombre del producto a buscar: ")
            # Busca el producto en el inventario.
            producto = servicios.buscar_producto(inventario, nombre_busqueda)
            if producto:
                print(f"Encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['cantidad']}")
            else:
                print("Producto no encontrado.")
                
        #Actualizar el precio y cantidad de un producto
        elif opcion == "4":
            nombre_editar = input("Ingrese el nombre del producto a actualizar (o escriba 'atras'): ")
            if nombre_editar.lower() != "atras":
                producto = servicios.buscar_producto(inventario, nombre_editar)
                if producto:
                    print(f"Editando: {producto['nombre']} (Precio: ${producto['precio']}, Stock: {producto['cantidad']})")
                    datos_validos = False
                    
                    while not datos_validos:
                        print("\n--- Menú de Actualización ---")
                        print("Ingrese los nuevos datos (o use '-1' para cancelar)")
                        
                        # Validación del nuevo precio.
                        nuevo_precio = 0
                        while nuevo_precio <= 0:
                            try:
                                nuevo_precio = float(input("Nuevo Precio: "))
                                if nuevo_precio == -1:
                                    datos_validos = True
                                    break
                                if nuevo_precio <= 0:
                                    print("Error: el precio debe ser mayor a 0.")
                            except ValueError:
                                print("Error: ingrese un número válido.")

                        # Validación de nueva cantidad.
                        nueva_cantidad = 0
                        while nueva_cantidad <= 0:
                            try:
                                entrada = input("Nueva Cantidad: ")
                                if "." in entrada:
                                    print("Error: la cantidad debe ser un número entero.")
                                    continue
                                
                                nueva_cantidad = int(entrada)
                                if nueva_cantidad == -1:
                                    datos_validos = True
                                    break
                                if nueva_cantidad <= 0:
                                    print("Error: la cantidad debe ser mayor a 0.")
                            except ValueError:
                                print("Error: ingrese un número entero válido.")

                        # Actualiza el producto en el inventario.
                        producto['precio'] = nuevo_precio
                        producto['cantidad'] = nueva_cantidad
                        print("Producto actualizado con éxito.")
                        datos_validos = True
                else:
                    print(f"Error: El producto '{nombre_editar}' no existe.")
        
        #Elimina el producto y devuelve el resultado 
        elif opcion == "5":
            nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")

            exito = servicios.eliminar_producto(inventario, nombre_eliminar)
            if exito:
                print(f"Producto '{nombre_eliminar}' eliminado correctamente.")
            else:
                print("No se pudo eliminar: El producto no existe.")

        # Calcular y muestrar estadísticas del inventario.
        elif opcion == "6":
            
            stats = servicios.calcular_estadisticas(inventario)
            if stats:
                print(f"--- ESTADÍSTICAS ---")
                print(f"Unidades totales: {stats['unidades']}")
                print(f"Valor Total: ${stats['valor']}")
                print(f"Más caro: {stats['caro']['nombre']} (${stats['caro']['precio']})")
                print(f"Mayor stock: {stats['stock']['nombre']} ({stats['stock']['cantidad']} unds)")
            else:
                print("El inventario está vacío.")

        # Guarda el inventario en un archivo CSV 
        
        elif opcion == "7":

            archivos.guardar_csv(inventario)
            
        #Cargan los datos desde un archivo CSV y se decide si el producto ya existe
        elif opcion == "8":
            # Carga datos desde un archivo CSV.
            datos, era = archivos.cargar_csv()
            if datos or era > 0:
                sobre = input("¿Sobrescribir inventario actual? (S/N): ").upper()

                if sobre == "S":
                    inventario = datos
                else:
                    for d in datos:
                        existente = servicios.buscar_producto(inventario, d["nombre"])

                        if existente:
                            existente["cantidad"] += d["cantidad"]
                            existente["precio"] = d["precio"]
                        else:
                            inventario.append(d)
                print(f"Carga finalizada: {era}")

        # SALIR
        elif opcion == "9":
            print("Saliendo del sistema...")
            
        else:
            print("Opción no válida. Intente de nuevo.")
#Esta línea verifica si el archivo se está ejecutando directamente. 
# Si es así, llama a la función `ejecutar_menu()` para iniciar el sistema de inventario.
# Esto evita que el código se ejecute si el archivo es importado en otro programa.
if __name__ == "__main__":
    ejecutar_menu()
